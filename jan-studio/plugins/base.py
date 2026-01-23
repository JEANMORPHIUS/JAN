"""
JAN Plugin Base Interface

Base class and interfaces for JAN plugins.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
from enum import Enum


class PluginType(Enum):
    """Plugin type enumeration."""
    AI_SERVICE = "ai-service"
    OUTPUT_FORMAT = "output-format"
    VALIDATOR = "validator"
    INTEGRATION = "integration"


class JANPlugin(ABC):
    """
    Base class for all JAN plugins.
    
    All plugins must inherit from this class and implement
    the required methods.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize plugin with optional configuration."""
        self.config = config or {}
        self._enabled = True
    
    @abstractmethod
    def name(self) -> str:
        """Return the plugin name."""
        pass
    
    @abstractmethod
    def version(self) -> str:
        """Return the plugin version."""
        pass
    
    @abstractmethod
    def plugin_type(self) -> PluginType:
        """Return the plugin type."""
        pass
    
    def description(self) -> str:
        """Return plugin description (optional)."""
        return ""
    
    def author(self) -> str:
        """Return plugin author (optional)."""
        return "Unknown"
    
    def dependencies(self) -> List[str]:
        """Return list of required dependencies (optional)."""
        return []
    
    def permissions(self) -> List[str]:
        """Return list of required permissions (optional)."""
        return []
    
    def is_enabled(self) -> bool:
        """Check if plugin is enabled."""
        return self._enabled
    
    def enable(self):
        """Enable the plugin."""
        self._enabled = True
    
    def disable(self):
        """Disable the plugin."""
        self._enabled = False
    
    def configure(self, config: Dict[str, Any]):
        """Update plugin configuration."""
        self.config.update(config)
    
    def validate_config(self) -> tuple[bool, Optional[str]]:
        """Validate plugin configuration. Returns (is_valid, error_message)."""
        return True, None
    
    def initialize(self) -> bool:
        """Initialize plugin. Called after loading. Returns success status."""
        return True
    
    def cleanup(self):
        """Cleanup plugin resources. Called before unloading."""
        pass


class AIServicePlugin(JANPlugin):
    """
    Base class for AI service plugins.
    
    Provides interface for integrating new LLM providers.
    """
    
    def plugin_type(self) -> PluginType:
        return PluginType.AI_SERVICE
    
    @abstractmethod
    def generate(
        self,
        prompt: str,
        persona: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Generate content using the AI service.
        
        Args:
            prompt: The input prompt
            persona: Persona configuration
            context: Additional context
            options: Generation options (temperature, max_tokens, etc.)
        
        Returns:
            Dict with 'content' and optional metadata
        """
        pass
    
    def supports_streaming(self) -> bool:
        """Check if plugin supports streaming responses."""
        return False
    
    def stream_generate(
        self,
        prompt: str,
        persona: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None,
        options: Optional[Dict[str, Any]] = None
    ):
        """
        Generate content with streaming (if supported).
        
        Yields chunks of content as they're generated.
        """
        raise NotImplementedError("Streaming not supported")


class OutputFormatPlugin(JANPlugin):
    """
    Base class for output format plugins.
    
    Provides interface for custom output formats.
    """
    
    def plugin_type(self) -> PluginType:
        return PluginType.OUTPUT_FORMAT
    
    @abstractmethod
    def format_name(self) -> str:
        """Return the format name (e.g., 'json', 'xml', 'markdown')."""
        pass
    
    @abstractmethod
    def process(
        self,
        content: str,
        persona: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Process content into the specified format.
        
        Args:
            content: Raw content to format
            persona: Persona configuration
            context: Additional context
        
        Returns:
            Dict with 'formatted_content' and optional metadata
        """
        pass
    
    def validate(self, content: str) -> tuple[bool, Optional[str]]:
        """
        Validate content matches the format.
        
        Returns:
            (is_valid, error_message)
        """
        return True, None


class ValidatorPlugin(JANPlugin):
    """
    Base class for validation plugins.
    
    Provides interface for custom validation rules.
    """
    
    def plugin_type(self) -> PluginType:
        return PluginType.VALIDATOR
    
    @abstractmethod
    def validate(
        self,
        output: str,
        rules: Dict[str, Any],
        persona: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> tuple[bool, List[str], List[str]]:
        """
        Validate output against rules.
        
        Args:
            output: Content to validate
            rules: Validation rules
            persona: Persona configuration
            context: Additional context
        
        Returns:
            (is_valid, errors, warnings)
        """
        pass
    
    @abstractmethod
    def rule_name(self) -> str:
        """Return the name of the validation rule."""
        pass


class IntegrationPlugin(JANPlugin):
    """
    Base class for integration plugins.
    
    Provides interface for external API integrations.
    """
    
    def plugin_type(self) -> PluginType:
        return PluginType.INTEGRATION
    
    @abstractmethod
    def process(
        self,
        persona: Dict[str, Any],
        prompt: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Process request through integration.
        
        Args:
            persona: Persona configuration
            prompt: Input prompt
            context: Additional context
        
        Returns:
            Dict with results
        """
        pass
    
    @abstractmethod
    def service_name(self) -> str:
        """Return the name of the integrated service."""
        pass

