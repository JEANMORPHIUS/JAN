"""
JAN Plugin Manager

High-level plugin management and integration with JAN system.
"""

from typing import Dict, Any, Optional, List
from plugins.loader import PluginLoader, get_loader
from plugins.base import PluginType, AIServicePlugin, OutputFormatPlugin, ValidatorPlugin, IntegrationPlugin


class PluginManager:
    """Manages plugins and provides high-level interface."""
    
    def __init__(self):
        """Initialize plugin manager."""
        self.loader = get_loader()
    
    def get_ai_service(self, name: Optional[str] = None) -> Optional[AIServicePlugin]:
        """Get AI service plugin."""
        if name:
            plugin = self.loader.get_plugin(name)
            if isinstance(plugin, AIServicePlugin):
                return plugin
            return None
        
        # Get first available AI service
        ai_services = self.loader.get_plugins_by_type(PluginType.AI_SERVICE)
        return ai_services[0] if ai_services else None
    
    def get_output_formatter(self, format_name: str) -> Optional[OutputFormatPlugin]:
        """Get output format plugin by format name."""
        formatters = self.loader.get_plugins_by_type(PluginType.OUTPUT_FORMAT)
        for formatter in formatters:
            if formatter.format_name() == format_name:
                return formatter
        return None
    
    def get_validators(self) -> List[ValidatorPlugin]:
        """Get all validator plugins."""
        return [
            plugin for plugin in self.loader.get_plugins_by_type(PluginType.VALIDATOR)
            if isinstance(plugin, ValidatorPlugin)
        ]
    
    def get_integration(self, service_name: str) -> Optional[IntegrationPlugin]:
        """Get integration plugin by service name."""
        integrations = self.loader.get_plugins_by_type(PluginType.INTEGRATION)
        for integration in integrations:
            if integration.service_name() == service_name:
                return integration
        return None
    
    def generate_with_ai(
        self,
        prompt: str,
        persona: Dict[str, Any],
        ai_service: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Generate content using AI service plugin."""
        plugin = self.get_ai_service(ai_service)
        if not plugin:
            return {
                "error": "No AI service plugin available",
                "content": None
            }
        
        return plugin.generate(prompt, persona, context, options)
    
    def format_output(
        self,
        content: str,
        format_name: str,
        persona: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Format output using format plugin."""
        plugin = self.get_output_formatter(format_name)
        if not plugin:
            return {
                "error": f"Output format '{format_name}' not available",
                "formatted_content": content
            }
        
        return plugin.process(content, persona, context)
    
    def validate_output(
        self,
        output: str,
        rules: Dict[str, Any],
        persona: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Validate output using all validator plugins."""
        validators = self.get_validators()
        
        all_valid = True
        all_errors = []
        all_warnings = []
        
        for validator in validators:
            rule_name = validator.rule_name()
            if rule_name in rules:
                is_valid, errors, warnings = validator.validate(
                    output, rules[rule_name], persona, context
                )
                
                if not is_valid:
                    all_valid = False
                
                all_errors.extend(errors)
                all_warnings.extend(warnings)
        
        return {
            "valid": all_valid,
            "errors": all_errors,
            "warnings": all_warnings
        }
    
    def call_integration(
        self,
        service_name: str,
        persona: Dict[str, Any],
        prompt: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Call integration plugin."""
        plugin = self.get_integration(service_name)
        if not plugin:
            return {
                "error": f"Integration '{service_name}' not available",
                "success": False
            }
        
        return plugin.process(persona, prompt, context)
    
    def list_plugins(self) -> List[Dict[str, Any]]:
        """List all plugins."""
        return self.loader.list_plugins()
    
    def reload_plugins(self):
        """Reload all plugins."""
        self.loader = PluginLoader()
        self.loader.load_all_plugins()


# Global plugin manager instance
_manager: Optional[PluginManager] = None


def get_manager() -> PluginManager:
    """Get the global plugin manager instance."""
    global _manager
    if _manager is None:
        _manager = PluginManager()
    return _manager

