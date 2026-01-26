"""JAN Plugin Loader

Loads and manages plugins from the plugin directory.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import os
import json
import importlib.util
from pathlib import Path
from typing import Dict, List, Optional, Type
from base import JANPlugin, PluginType

PLUGINS_DIR = os.getenv("JAN_PLUGINS_DIR", os.path.join(os.path.dirname(__file__), "..", "plugins"))


class PluginLoader:
    """Loads and manages JAN plugins."""
    
    def __init__(self, plugins_dir: Optional[str] = None):
        """Initialize plugin loader."""
        self.plugins_dir = Path(plugins_dir or PLUGINS_DIR)
        self.plugins: Dict[str, JANPlugin] = {}
        self.plugin_metadata: Dict[str, Dict[str, Any]] = {}
    
    def discover_plugins(self) -> List[str]:
        """Discover all plugins in the plugins directory."""
        plugin_paths = []
        
        # Search in plugin type directories
        plugin_type_dirs = [
            "ai-services",
            "output-formats",
            "validators",
            "integrations"
        ]
        
        for plugin_type_dir in plugin_type_dirs:
            type_path = self.plugins_dir / plugin_type_dir
            if not type_path.exists():
                continue
            
            # Find all plugin.json files
            for plugin_json in type_path.rglob("plugin.json"):
                plugin_paths.append(str(plugin_json.parent))
        
        return plugin_paths
    
    def load_plugin(self, plugin_path: str) -> Optional[JANPlugin]:
        """Load a plugin from a directory."""
        plugin_dir = Path(plugin_path)
        manifest_path = plugin_dir / "plugin.json"
        
        if not manifest_path.exists():
            return None
        
        try:
            # Load manifest
            with open(manifest_path, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
            
            # Validate manifest
            required_fields = ["name", "version", "entry_point"]
            for field in required_fields:
                if field not in manifest:
                    print(f"⚠️  Plugin {plugin_path} missing required field: {field}")
                    return None
            
            # Load plugin module
            entry_point = manifest["entry_point"]
            module_path = plugin_dir / entry_point
            
            if not module_path.exists():
                print(f"⚠️  Plugin {plugin_path} entry point not found: {entry_point}")
                return None
            
            # Import module
            spec = importlib.util.spec_from_file_location(
                manifest["name"],
                module_path
            )
            if spec is None or spec.loader is None:
                print(f"⚠️  Failed to load plugin module: {entry_point}")
                return None
            
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Find plugin class
            plugin_class = None
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if (isinstance(attr, type) and 
                    issubclass(attr, JANPlugin) and 
                    attr != JANPlugin):
                    plugin_class = attr
                    break
            
            if plugin_class is None:
                print(f"⚠️  No plugin class found in {entry_point}")
                return None
            
            # Create plugin instance
            config = manifest.get("config", {})
            plugin = plugin_class(config)
            
            # Validate configuration
            is_valid, error = plugin.validate_config()
            if not is_valid:
                print(f"⚠️  Plugin {manifest['name']} config invalid: {error}")
                return None
            
            # Initialize plugin
            if not plugin.initialize():
                print(f"⚠️  Plugin {manifest['name']} initialization failed")
                return None
            
            # Store plugin
            plugin_name = manifest["name"]
            self.plugins[plugin_name] = plugin
            self.plugin_metadata[plugin_name] = manifest
            
            print(f"✅ Loaded plugin: {plugin_name} v{manifest['version']}")
            return plugin
        
        except Exception as e:
            print(f"❌ Error loading plugin {plugin_path}: {e}")
            return None
    
    def load_all_plugins(self) -> Dict[str, JANPlugin]:
        """Load all discovered plugins."""
        plugin_paths = self.discover_plugins()
        
        for plugin_path in plugin_paths:
            self.load_plugin(plugin_path)
        
        return self.plugins
    
    def get_plugin(self, name: str) -> Optional[JANPlugin]:
        """Get a loaded plugin by name."""
        return self.plugins.get(name)
    
    def get_plugins_by_type(self, plugin_type: PluginType) -> List[JANPlugin]:
        """Get all plugins of a specific type."""
        return [
            plugin for plugin in self.plugins.values()
            if plugin.plugin_type() == plugin_type and plugin.is_enabled()
        ]
    
    def unload_plugin(self, name: str) -> bool:
        """Unload a plugin."""
        if name not in self.plugins:
            return False
        
        plugin = self.plugins[name]
        plugin.cleanup()
        del self.plugins[name]
        del self.plugin_metadata[name]
        
        return True
    
    def list_plugins(self) -> List[Dict[str, Any]]:
        """List all loaded plugins with metadata."""
        result = []
        for name, plugin in self.plugins.items():
            metadata = self.plugin_metadata.get(name, {})
            result.append({
                "name": name,
                "version": plugin.version(),
                "type": plugin.plugin_type().value,
                "enabled": plugin.is_enabled(),
                "author": plugin.author(),
                "description": plugin.description(),
                "metadata": metadata
            })
        return result


# Global plugin loader instance
_loader: Optional[PluginLoader] = None


def get_loader() -> PluginLoader:
    """Get the global plugin loader instance."""
    global _loader
    if _loader is None:
        _loader = PluginLoader()
        _loader.load_all_plugins()
    return _loader

