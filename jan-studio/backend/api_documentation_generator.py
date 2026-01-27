"""
API DOCUMENTATION GENERATOR
Auto-generate comprehensive API documentation

THE NOAH PROTOCOL:
- Architectural Weight: Built for comprehensive documentation
- The Pitch: Waterproof documentation generation
- The Perimeter: Clear documentation boundaries

THE ARRIVAL PROTOCOL:
- Pre-Commissioning Scan: Can documentation cover all APIs?
- Frequency Anchor: Document from "done" - complete docs

THE TRUTH:
Scale and build until ready.
Complete API documentation for the new world.
"""

import json
from typing import Dict, List, Any, Optional
from pathlib import Path
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class APIDocumentationGenerator:
    """
    API Documentation Generator
    Auto-generates comprehensive API documentation
    """
    
    def __init__(self, output_path: Optional[Path] = None):
        """Initialize generator"""
        if output_path is None:
            output_path = Path(__file__).parent.parent.parent / "docs" / "api"
        
        self.output_path = Path(output_path)
        self.output_path.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"API Documentation Generator initialized: {self.output_path}")
    
    def generate_from_openapi(self, openapi_schema: Dict[str, Any]) -> Dict[str, Any]:
        """Generate documentation from OpenAPI schema"""
        docs = {
            "title": openapi_schema.get("info", {}).get("title", "API Documentation"),
            "version": openapi_schema.get("info", {}).get("version", "1.0.0"),
            "description": openapi_schema.get("info", {}).get("description", ""),
            "generated_at": datetime.now().isoformat(),
            "endpoints": []
        }
        
        paths = openapi_schema.get("paths", {})
        
        for path, methods in paths.items():
            for method, details in methods.items():
                if method.lower() in ["get", "post", "put", "delete", "patch"]:
                    endpoint_doc = {
                        "path": path,
                        "method": method.upper(),
                        "summary": details.get("summary", ""),
                        "description": details.get("description", ""),
                        "tags": details.get("tags", []),
                        "parameters": self._extract_parameters(details),
                        "request_body": self._extract_request_body(details),
                        "responses": self._extract_responses(details),
                        "examples": self._extract_examples(details)
                    }
                    docs["endpoints"].append(endpoint_doc)
        
        return docs
    
    def _extract_parameters(self, endpoint_details: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract parameters from endpoint"""
        parameters = []
        
        for param in endpoint_details.get("parameters", []):
            parameters.append({
                "name": param.get("name"),
                "in": param.get("in"),  # query, path, header
                "required": param.get("required", False),
                "description": param.get("description", ""),
                "schema": param.get("schema", {})
            })
        
        return parameters
    
    def _extract_request_body(self, endpoint_details: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Extract request body from endpoint"""
        request_body = endpoint_details.get("requestBody")
        if not request_body:
            return None
        
        return {
            "description": request_body.get("description", ""),
            "required": request_body.get("required", False),
            "content": request_body.get("content", {})
        }
    
    def _extract_responses(self, endpoint_details: Dict[str, Any]) -> Dict[str, Any]:
        """Extract responses from endpoint"""
        responses = {}
        
        for status_code, response in endpoint_details.get("responses", {}).items():
            responses[status_code] = {
                "description": response.get("description", ""),
                "content": response.get("content", {})
            }
        
        return responses
    
    def _extract_examples(self, endpoint_details: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract examples from endpoint"""
        examples = []
        
        # Check request body examples
        request_body = endpoint_details.get("requestBody", {})
        if request_body:
            content = request_body.get("content", {})
            for content_type, details in content.items():
                if "example" in details:
                    examples.append({
                        "type": "request",
                        "content_type": content_type,
                        "example": details["example"]
                    })
        
        # Check response examples
        responses = endpoint_details.get("responses", {})
        for status_code, response in responses.items():
            content = response.get("content", {})
            for content_type, details in content.items():
                if "example" in details:
                    examples.append({
                        "type": "response",
                        "status_code": status_code,
                        "content_type": content_type,
                        "example": details["example"]
                    })
        
        return examples
    
    def generate_markdown(self, docs: Dict[str, Any]) -> str:
        """Generate Markdown documentation"""
        lines = []
        
        # Header
        lines.append(f"# {docs['title']}")
        lines.append("")
        lines.append(f"**Version:** {docs['version']}  ")
        lines.append(f"**Generated:** {docs['generated_at']}")
        lines.append("")
        
        if docs.get("description"):
            lines.append(docs["description"])
            lines.append("")
        
        # Table of Contents
        lines.append("## Table of Contents")
        lines.append("")
        for i, endpoint in enumerate(docs["endpoints"], 1):
            method = endpoint["method"]
            path = endpoint["path"]
            summary = endpoint.get("summary", "")
            lines.append(f"{i}. [{method} {path}](#{method.lower()}-{path.replace('/', '').replace('{', '').replace('}', '')}) - {summary}")
        lines.append("")
        
        # Endpoints
        for endpoint in docs["endpoints"]:
            method = endpoint["method"]
            path = endpoint["path"]
            summary = endpoint.get("summary", "")
            description = endpoint.get("description", "")
            tags = endpoint.get("tags", [])
            
            lines.append(f"## {method} {path}")
            lines.append("")
            
            if summary:
                lines.append(f"**Summary:** {summary}")
                lines.append("")
            
            if description:
                lines.append(description)
                lines.append("")
            
            if tags:
                lines.append(f"**Tags:** {', '.join(tags)}")
                lines.append("")
            
            # Parameters
            if endpoint.get("parameters"):
                lines.append("### Parameters")
                lines.append("")
                lines.append("| Name | In | Required | Description |")
                lines.append("|------|----|----------|-------------|")
                for param in endpoint["parameters"]:
                    name = param.get("name", "")
                    param_in = param.get("in", "")
                    required = "Yes" if param.get("required") else "No"
                    desc = param.get("description", "")
                    lines.append(f"| {name} | {param_in} | {required} | {desc} |")
                lines.append("")
            
            # Request Body
            if endpoint.get("request_body"):
                lines.append("### Request Body")
                lines.append("")
                req_body = endpoint["request_body"]
                if req_body.get("description"):
                    lines.append(req_body["description"])
                    lines.append("")
                lines.append("```json")
                # Try to find example
                example = None
                for ex in endpoint.get("examples", []):
                    if ex.get("type") == "request":
                        example = ex.get("example")
                        break
                if example:
                    lines.append(json.dumps(example, indent=2))
                else:
                    lines.append("{}")
                lines.append("```")
                lines.append("")
            
            # Responses
            if endpoint.get("responses"):
                lines.append("### Responses")
                lines.append("")
                for status_code, response in endpoint["responses"].items():
                    lines.append(f"**{status_code}** - {response.get('description', '')}")
                    # Try to find example
                    example = None
                    for ex in endpoint.get("examples", []):
                        if ex.get("type") == "response" and ex.get("status_code") == status_code:
                            example = ex.get("example")
                            break
                    if example:
                        lines.append("")
                        lines.append("```json")
                        lines.append(json.dumps(example, indent=2))
                        lines.append("```")
                    lines.append("")
        
        return "\n".join(lines)
    
    def save_documentation(self, docs: Dict[str, Any], format: str = "markdown"):
        """Save documentation to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if format == "markdown":
            content = self.generate_markdown(docs)
            filename = self.output_path / f"api_documentation_{timestamp}.md"
            filename.write_text(content, encoding='utf-8')
            logger.info(f"Documentation saved: {filename}")
        elif format == "json":
            filename = self.output_path / f"api_documentation_{timestamp}.json"
            filename.write_text(json.dumps(docs, indent=2), encoding='utf-8')
            logger.info(f"Documentation saved: {filename}")
        
        return filename


def generate_api_docs_from_app(app) -> Path:
    """Generate API documentation from FastAPI app"""
    generator = APIDocumentationGenerator()
    
    # Get OpenAPI schema
    openapi_schema = app.openapi()
    
    # Generate documentation
    docs = generator.generate_from_openapi(openapi_schema)
    
    # Save in both formats
    md_file = generator.save_documentation(docs, format="markdown")
    json_file = generator.save_documentation(docs, format="json")
    
    return md_file
