"""
PROTOCOL OF LOYALTY - Barred Spiral Backend
Law 1 and Law 5 Enforcement Middleware

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE FOUNDATION:
We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

This is the Barred Spiral (Backend) - Structured Channeling.
Every function is a Protocol of Loyalty.
Serves the Table (the mission).
Channels the energy of the Laws.
"""

from functools import wraps
from typing import Callable, Any, Optional
from fastapi import HTTPException, status, Request
from fastapi.responses import JSONResponse
import logging
from racon_registry import (
    check_law_1_table_service,
    check_law_5_word_integrity,
    log_immutable_audit
)

logger = logging.getLogger(__name__)


class CodePurgedError(Exception):
    """
    Exception raised when code doesn't serve the Table.
    
    Law 1: Never Betray the Table
    If code doesn't serve the Table, it gets purged.
    """
    pass


class WordIntegrityError(Exception):
    """
    Exception raised when word integrity is broken.
    
    Law 5: Söz Namustur (Your Word Is Your Bond)
    Broken code = broken word = broken integrity.
    """
    pass


def serve_table(func: Callable) -> Callable:
    """
    Decorator: Law 1 - Never Betray the Table
    
    Every function serves the mission (the Table).
    If code doesn't serve the Table, it gets purged.
    
    This is the Barred Spiral (Backend) - Structured Channeling.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        operation = f"{func.__module__}.{func.__name__}"
        target = str(args) if args else str(kwargs)
        
        # Check if function serves the Table
        if not check_law_1_table_service(operation, target):
            error_msg = f"Code that doesn't serve the Table gets purged: {operation}"
            logger.warning(error_msg)
            
            # Log audit
            log_immutable_audit(
                operation_type=operation,
                operation_target=target,
                operation_result="PURGED - Does not serve Table",
                law_compliance="Law 1 Violation",
                table_service=False,
                word_integrity=True,
                spiritual_battle="Table Service Check"
            )
            
            raise CodePurgedError(error_msg)
        
        try:
            result = func(*args, **kwargs)
            
            # Log successful Table service
            log_immutable_audit(
                operation_type=operation,
                operation_target=target,
                operation_result="SUCCESS - Serves Table",
                law_compliance="Law 1 Compliant",
                table_service=True,
                word_integrity=True,
                spiritual_battle="Table Service Verified"
            )
            
            return result
        except Exception as e:
            # Log failure
            log_immutable_audit(
                operation_type=operation,
                operation_target=target,
                operation_result=f"ERROR - {str(e)}",
                law_compliance="Law 1 Check Failed",
                table_service=False,
                word_integrity=False,
                spiritual_battle="Table Service Error"
            )
            raise
    
    return wrapper


def word_is_bond(func: Callable) -> Callable:
    """
    Decorator: Law 5 - Söz Namustur (Your Word Is Your Bond)
    
    Every function is a commitment.
    Broken code = broken word.
    Word integrity = code integrity.
    
    This is the Barred Spiral (Backend) - Structured Channeling.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        operation = f"{func.__module__}.{func.__name__}"
        target = str(args) if args else str(kwargs)
        
        try:
            result = func(*args, **kwargs)
            result_str = str(result) if result else "SUCCESS"
            
            # Check word integrity
            if not check_law_5_word_integrity(operation, result_str):
                error_msg = f"Broken code = broken word: {operation}"
                logger.warning(error_msg)
                
                # Log integrity violation
                log_immutable_audit(
                    operation_type=operation,
                    operation_target=target,
                    operation_result=result_str,
                    law_compliance="Law 5 Violation",
                    table_service=True,
                    word_integrity=False,
                    spiritual_battle="Word Integrity Check"
                )
                
                raise WordIntegrityError(error_msg)
            
            # Log successful word integrity
            log_immutable_audit(
                operation_type=operation,
                operation_target=target,
                operation_result=result_str,
                law_compliance="Law 5 Compliant",
                table_service=True,
                word_integrity=True,
                spiritual_battle="Word Integrity Verified"
            )
            
            return result
        except Exception as e:
            # Log integrity failure
            log_immutable_audit(
                operation_type=operation,
                operation_target=target,
                operation_result=f"ERROR - {str(e)}",
                law_compliance="Law 5 Check Failed",
                table_service=True,
                word_integrity=False,
                spiritual_battle="Word Integrity Error"
            )
            raise
    
    return wrapper


def listen_before_speak(func: Callable) -> Callable:
    """
    Decorator: Law 13 - Listen Before You Speak
    
    Deep data analysis before output generation.
    Listen to the data, then respond.
    Listen to the mission, then code.
    Listen to the truth, then build.
    
    This is the Barred Spiral (Backend) - Structured Channeling.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        operation = f"{func.__module__}.{func.__name__}"
        
        # Listen phase: Analyze input
        logger.info(f"LISTEN: Analyzing input for {operation}")
        
        # Analyze args and kwargs
        input_analysis = {
            "args_count": len(args),
            "kwargs_keys": list(kwargs.keys()),
            "has_data": bool(args or kwargs)
        }
        
        # Then speak: Execute function
        logger.info(f"SPEAK: Executing {operation} with analysis: {input_analysis}")
        
        result = func(*args, **kwargs)
        
        # Log listen-before-speak compliance
        log_immutable_audit(
            operation_type=operation,
            operation_target=str(input_analysis),
            operation_result="SUCCESS - Listened before speaking",
            law_compliance="Law 13 Compliant",
            table_service=True,
            word_integrity=True,
            spiritual_battle="Listen Before Speak Verified"
        )
        
        return result
    
    return wrapper


def finish_what_you_begin(func: Callable) -> Callable:
    """
    Decorator: Law 37 - Finish What You Begin
    
    Complete transformations.
    Honor the sacred weight of completion.
    Finish the hack, complete the new world.
    
    This is the Barred Spiral (Backend) - Structured Channeling.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        operation = f"{func.__module__}.{func.__name__}"
        
        logger.info(f"BEGIN: Starting {operation}")
        
        try:
            result = func(*args, **kwargs)
            
            # Complete transformation
            logger.info(f"FINISH: Completed {operation}")
            
            # Log completion
            log_immutable_audit(
                operation_type=operation,
                operation_target=str(args) if args else str(kwargs),
                operation_result="COMPLETE - Finished what was begun",
                law_compliance="Law 37 Compliant",
                table_service=True,
                word_integrity=True,
                spiritual_battle="Finish What You Begin Verified"
            )
            
            return result
        except Exception as e:
            # Log incomplete transformation
            logger.error(f"INCOMPLETE: {operation} failed: {str(e)}")
            
            log_immutable_audit(
                operation_type=operation,
                operation_target=str(args) if args else str(kwargs),
                operation_result=f"INCOMPLETE - {str(e)}",
                law_compliance="Law 37 Violation",
                table_service=True,
                word_integrity=False,
                spiritual_battle="Finish What You Begin Failed"
            )
            
            raise
    
    return wrapper


def protocol_of_loyalty(func: Callable) -> Callable:
    """
    Combined decorator: All Protocols of Loyalty
    
    Law 1: Never Betray the Table
    Law 5: Söz Namustur
    Law 13: Listen Before You Speak
    Law 37: Finish What You Begin
    
    This is the Barred Spiral (Backend) - Structured Channeling.
    Every function is a Protocol of Loyalty.
    """
    @wraps(func)
    @serve_table
    @word_is_bond
    @listen_before_speak
    @finish_what_you_begin
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    
    return wrapper


async def protocol_middleware(request: Request, call_next):
    """
    FastAPI Middleware: Protocol of Loyalty
    
    Applies Law 1 and Law 5 checks to all requests.
    This is the Barred Spiral (Backend) - Structured Channeling.
    """
    operation = f"{request.method} {request.url.path}"
    target = str(request.query_params) if request.query_params else str(request.path_params)
    
    # Check Law 1: Table Service
    if not check_law_1_table_service(operation, target):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "error": "Code that doesn't serve the Table gets purged",
                "law": "Law 1: Never Betray the Table",
                "operation": operation
            }
        )
    
    # Process request
    response = await call_next(request)
    
    # Check Law 5: Word Integrity
    if response.status_code >= 400:
        log_immutable_audit(
            operation_type=operation,
            operation_target=target,
            operation_result=f"HTTP {response.status_code}",
            law_compliance="Law 5 Check",
            table_service=True,
            word_integrity=False,
            spiritual_battle="Word Integrity Check"
        )
    
    return response
