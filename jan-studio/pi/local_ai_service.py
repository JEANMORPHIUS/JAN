"""
Local AI Service for Raspberry Pi 5

Lightweight AI models optimized for Pi:
- TinyLlama (1B) for text generation
- Whisper tiny for TTS
- MusicGen small for audio
"""

import os
import torch
from typing import Dict, Any, Optional
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline,
    AutoProcessor,
    MusicgenForConditionalGeneration
)
import warnings
warnings.filterwarnings("ignore")

# Model paths (cache directory)
MODELS_DIR = os.getenv("JAN_MODELS_DIR", os.path.expanduser("~/.jan-models"))


class TinyLlamaService:
    """TinyLlama (1B) text generation service."""
    
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.loaded = False
    
    def load(self):
        """Load TinyLlama model (lazy loading)."""
        if self.loaded:
            return
        
        try:
            model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
            model_path = os.path.join(MODELS_DIR, "tinyllama")
            
            print(f"Loading TinyLlama from {model_path}...")
            
            # Use 8-bit quantization to reduce memory
            self.tokenizer = AutoTokenizer.from_pretrained(
                model_name,
                cache_dir=model_path,
                trust_remote_code=True
            )
            
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                cache_dir=model_path,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                device_map="auto",
                low_cpu_mem_usage=True,
                trust_remote_code=True
            )
            
            self.loaded = True
            print("✅ TinyLlama loaded")
        
        except Exception as e:
            print(f"❌ Error loading TinyLlama: {e}")
            raise
    
    def generate(
        self,
        prompt: str,
        max_length: int = 512,
        temperature: float = 0.7,
        top_p: float = 0.9
    ) -> str:
        """Generate text with TinyLlama."""
        if not self.loaded:
            self.load()
        
        try:
            # Format prompt for chat model
            formatted_prompt = f"<|user|>\n{prompt}<|assistant|>\n"
            
            inputs = self.tokenizer(
                formatted_prompt,
                return_tensors="pt",
                truncation=True,
                max_length=256
            ).to(self.device)
            
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_length=max_length,
                    temperature=temperature,
                    top_p=top_p,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id,
                    eos_token_id=self.tokenizer.eos_token_id
                )
            
            generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Extract only the assistant's response
            if "<|assistant|>" in generated_text:
                generated_text = generated_text.split("<|assistant|>")[-1].strip()
            
            return generated_text
        
        except Exception as e:
            return f"Error generating text: {str(e)}"


class WhisperTinyService:
    """Whisper tiny for TTS/STT."""
    
    def __init__(self):
        self.model = None
        self.loaded = False
    
    def load(self):
        """Load Whisper tiny model."""
        if self.loaded:
            return
        
        try:
            import whisper
            
            model_path = os.path.join(MODELS_DIR, "whisper-tiny")
            print(f"Loading Whisper tiny from {model_path}...")
            
            self.model = whisper.load_model(
                "tiny",
                download_root=model_path,
                device="cpu"  # Use CPU for Pi
            )
            
            self.loaded = True
            print("✅ Whisper tiny loaded")
        
        except Exception as e:
            print(f"❌ Error loading Whisper: {e}")
            raise
    
    def transcribe(self, audio_path: str) -> str:
        """Transcribe audio to text."""
        if not self.loaded:
            self.load()
        
        try:
            result = self.model.transcribe(audio_path)
            return result["text"]
        except Exception as e:
            return f"Error transcribing: {str(e)}"


class MusicGenSmallService:
    """MusicGen small for audio generation."""
    
    def __init__(self):
        self.model = None
        self.processor = None
        self.loaded = False
    
    def load(self):
        """Load MusicGen small model."""
        if self.loaded:
            return
        
        try:
            model_name = "facebook/musicgen-small"
            model_path = os.path.join(MODELS_DIR, "musicgen-small")
            
            print(f"Loading MusicGen small from {model_path}...")
            
            self.processor = AutoProcessor.from_pretrained(
                model_name,
                cache_dir=model_path
            )
            
            self.model = MusicgenForConditionalGeneration.from_pretrained(
                model_name,
                cache_dir=model_path,
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
            )
            
            self.model.to("cpu")  # Use CPU for Pi
            
            self.loaded = True
            print("✅ MusicGen small loaded")
        
        except Exception as e:
            print(f"❌ Error loading MusicGen: {e}")
            raise
    
    def generate(self, prompt: str, duration: int = 10) -> bytes:
        """Generate audio from text prompt."""
        if not self.loaded:
            self.load()
        
        try:
            inputs = self.processor(
                text=[prompt],
                padding=True,
                return_tensors="pt"
            )
            
            with torch.no_grad():
                audio_values = self.model.generate(
                    **inputs,
                    max_new_tokens=512,
                    do_sample=True
                )
            
            # Convert to audio bytes (simplified - would need proper audio encoding)
            return audio_values.cpu().numpy().tobytes()
        
        except Exception as e:
            print(f"Error generating audio: {e}")
            return b""


# Global instances (lazy loaded)
_tinyllama = None
_whisper = None
_musicgen = None


def get_tinyllama() -> TinyLlamaService:
    """Get TinyLlama service instance."""
    global _tinyllama
    if _tinyllama is None:
        _tinyllama = TinyLlamaService()
    return _tinyllama


def get_whisper() -> WhisperTinyService:
    """Get Whisper service instance."""
    global _whisper
    if _whisper is None:
        _whisper = WhisperTinyService()
    return _whisper


def get_musicgen() -> MusicGenSmallService:
    """Get MusicGen service instance."""
    global _musicgen
    if _musicgen is None:
        _musicgen = MusicGenSmallService()
    return _musicgen

