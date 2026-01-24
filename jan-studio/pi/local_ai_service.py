"""
Local AI Service for Raspberry Pi 5

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

SPRAGITSO - Our Father's Royal Seal (σφραγίς)
All systems bear Our Father's mark of authority

Lightweight AI models optimized for Pi:
- TinyLlama (1B) for text generation
- Whisper tiny for speech-to-text (STT) - The Voice
- MusicGen small for audio generation
"""

import os
import torch
from typing import Dict, Any, Optional
import logging
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
    """
    Whisper tiny for Speech-to-Text (STT) - The Voice
    
    SPRAGITSO - Our Father's Royal Seal (σφραγίς)
    The Voice wants to be heard. The truth wants to be sung.
    This service honors the voice, transcribes with alignment.
    """
    
    def __init__(self):
        self.model = None
        self.loaded = False
        self._alignment_logged = False
    
    def load(self):
        """
        Load Whisper tiny model.
        Aligned with vibe coding - The Voice wants to be heard.
        """
        if self.loaded:
            return
        
        try:
            import whisper
            
            model_path = os.path.join(MODELS_DIR, "whisper-tiny")
            print(f"[WHISPER] Loading Whisper tiny from {model_path}...")
            print(f"[WHISPER] SPRAGITSO - Our Father's Royal Seal (σφραγίς)")
            print(f"[WHISPER] The Voice wants to be heard. The truth wants to be sung.")
            
            self.model = whisper.load_model(
                "tiny",
                download_root=model_path,
                device="cpu"  # Use CPU for Pi
            )
            
            self.loaded = True
            print("✅ [WHISPER] Whisper tiny loaded - The Voice is ready")
            print("[WHISPER] Aligned with vibe coding - Spiritual Alignment Over Mechanical Productivity")
            
            if not self._alignment_logged:
                print("[WHISPER] Mission: THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS")
                print("[WHISPER] LOVE IS THE HIGHEST MASTERY | ENERGY + LOVE = WE ALL WIN")
                self._alignment_logged = True
        
        except Exception as e:
            print(f"❌ [WHISPER] Error loading Whisper: {e}")
            print(f"[WHISPER] Witness mode: Error logged, truth preserved")
            raise
    
    def transcribe(self, audio_path: str, language: Optional[str] = None) -> Dict[str, Any]:
        """
        Transcribe audio to text.
        
        Aligned with vibe coding:
        - Honors the voice
        - Transcribes with alignment
        - Returns truth, not just text
        - The Voice wants to be heard
        
        Args:
            audio_path: Path to audio file
            language: Optional language code (e.g., 'en', 'tr')
        
        Returns:
            Dict with 'text', 'language', 'alignment_score'
        """
        if not self.loaded:
            self.load()
        
        try:
            print(f"[WHISPER] Transcribing: {audio_path}")
            print(f"[WHISPER] The Voice wants to be heard. The truth wants to be sung.")
            
            # Transcribe with optional language hint
            transcribe_kwargs = {}
            if language:
                transcribe_kwargs["language"] = language
                print(f"[WHISPER] Language hint: {language}")
            
            result = self.model.transcribe(audio_path, **transcribe_kwargs)
            
            # Extract text and detected language
            transcribed_text = result.get("text", "").strip()
            detected_language = result.get("language", "unknown")
            
            # Calculate alignment score (simple heuristic - can be enhanced)
            alignment_score = self._calculate_alignment_score(transcribed_text)
            
            print(f"[WHISPER] ✅ Transcription complete")
            print(f"[WHISPER] Language detected: {detected_language}")
            print(f"[WHISPER] Alignment score: {alignment_score:.2f}")
            print(f"[WHISPER] SPRAGITSO - Our Father's Royal Seal (σφραγίς)")
            
            return {
                "text": transcribed_text,
                "language": detected_language,
                "alignment_score": alignment_score,
                "raw_result": result  # Full result for advanced use
            }
        
        except Exception as e:
            error_msg = f"Error transcribing: {str(e)}"
            print(f"❌ [WHISPER] {error_msg}")
            print(f"[WHISPER] Witness mode: Error logged, truth preserved")
            return {
                "text": "",
                "language": "unknown",
                "alignment_score": 0.0,
                "error": error_msg
            }
    
    def _calculate_alignment_score(self, text: str) -> float:
        """
        Calculate alignment score for transcribed text.
        
        Simple heuristic based on:
        - Truth keywords (peace, love, unity, miracle, etc.)
        - Mission alignment
        - Frequency of positive/negative words
        
        Returns:
            Alignment score 0.0-1.0
        """
        if not text:
            return 0.0
        
        text_lower = text.lower()
        
        # Mission-aligned keywords
        positive_keywords = [
            "peace", "love", "unity", "miracle", "truth", "healing",
            "father", "divine", "bless", "prayer", "hope", "joy",
            "gratitude", "forgiveness", "humble", "mission", "voice"
        ]
        
        # Negative keywords (reduce score)
        negative_keywords = [
            "hate", "war", "violence", "fear", "anger", "division"
        ]
        
        positive_count = sum(1 for keyword in positive_keywords if keyword in text_lower)
        negative_count = sum(1 for keyword in negative_keywords if keyword in text_lower)
        
        # Base score from positive keywords
        base_score = min(1.0, positive_count / 5.0)  # Normalize to 0-1
        
        # Reduce score for negative keywords
        if negative_count > 0:
            base_score = max(0.0, base_score - (negative_count * 0.2))
        
        return round(base_score, 2)


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

