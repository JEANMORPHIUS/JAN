"""
QUEUE SYSTEM
Architectural Weight: Built for 10x, 100x, 1000x scale

THE NOAH PROTOCOL:
- The Pitch: Waterproof error handling
- The Perimeter: Clear jurisdiction (queue management)
- The Door: Trust the queue's buoyancy (auto-retry)

THE TRUTH:
We build arks, not plastic tables.
"""

from typing import Optional, Any, Callable, Dict, List
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import asyncio
import logging
from functools import wraps

logger = logging.getLogger(__name__)


class TaskStatus(Enum):
    """Task status"""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    RETRYING = "retrying"


@dataclass
class QueueTask:
    """Queue task"""
    id: str
    function: Callable
    args: tuple = field(default_factory=tuple)
    kwargs: Dict[str, Any] = field(default_factory=dict)
    status: TaskStatus = TaskStatus.PENDING
    retries: int = 0
    max_retries: int = 3
    created_at: datetime = field(default_factory=datetime.now)
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error: Optional[str] = None


class QueueSystem:
    """
    Queue System
    Architectural Weight: Handles 10x, 100x, 1000x background tasks
    """
    
    def __init__(self, max_workers: int = 10):
        """
        Initialize queue system
        
        Args:
            max_workers: Maximum concurrent workers (Architectural Weight: 10 workers)
        """
        self.max_workers = max_workers
        self.queue: asyncio.Queue = asyncio.Queue()
        self.tasks: Dict[str, QueueTask] = {}
        self.workers: List[asyncio.Task] = []
        self.running = False
        
        logger.info(f"Queue system initialized: max_workers={max_workers}")
    
    async def start(self):
        """Start queue system (The Door: Trust the queue's buoyancy)"""
        if self.running:
            return
        
        self.running = True
        self.workers = [
            asyncio.create_task(self._worker(f"worker-{i}"))
            for i in range(self.max_workers)
        ]
        logger.info(f"Queue system started with {self.max_workers} workers")
    
    async def stop(self):
        """Stop queue system"""
        self.running = False
        
        # Wait for queue to empty
        await self.queue.join()
        
        # Cancel workers
        for worker in self.workers:
            worker.cancel()
        
        await asyncio.gather(*self.workers, return_exceptions=True)
        logger.info("Queue system stopped")
    
    async def enqueue(
        self,
        function: Callable,
        *args,
        task_id: Optional[str] = None,
        max_retries: int = 3,
        **kwargs
    ) -> str:
        """
        Enqueue task (The Perimeter: Clear jurisdiction)
        
        Args:
            function: Function to execute
            *args: Function arguments
            task_id: Optional task ID
            max_retries: Maximum retry attempts
            **kwargs: Function keyword arguments
        
        Returns:
            Task ID
        """
        if task_id is None:
            task_id = f"task-{datetime.now().timestamp()}"
        
        task = QueueTask(
            id=task_id,
            function=function,
            args=args,
            kwargs=kwargs,
            max_retries=max_retries
        )
        
        self.tasks[task_id] = task
        await self.queue.put(task)
        
        logger.info(f"Task enqueued: {task_id}")
        return task_id
    
    async def _worker(self, worker_name: str):
        """Worker process (The Pitch: Waterproof error handling)"""
        logger.info(f"Worker started: {worker_name}")
        
        while self.running:
            try:
                task = await self.queue.get()
                
                task.status = TaskStatus.PROCESSING
                task.started_at = datetime.now()
                
                try:
                    # Execute task
                    if asyncio.iscoroutinefunction(task.function):
                        result = await task.function(*task.args, **task.kwargs)
                    else:
                        result = task.function(*task.args, **task.kwargs)
                    
                    task.status = TaskStatus.COMPLETED
                    task.completed_at = datetime.now()
                    logger.info(f"Task completed: {task.id}")
                
                except Exception as e:
                    task.retries += 1
                    task.error = str(e)
                    
                    if task.retries < task.max_retries:
                        task.status = TaskStatus.RETRYING
                        logger.warning(f"Task failed, retrying ({task.retries}/{task.max_retries}): {task.id}")
                        await asyncio.sleep(2 ** task.retries)  # Exponential backoff
                        await self.queue.put(task)
                    else:
                        task.status = TaskStatus.FAILED
                        logger.error(f"Task failed after {task.max_retries} retries: {task.id}")
                
                finally:
                    self.queue.task_done()
            
            except asyncio.CancelledError:
                logger.info(f"Worker cancelled: {worker_name}")
                break
            except Exception as e:
                logger.error(f"Worker error: {worker_name}, {e}")
    
    def get_task_status(self, task_id: str) -> Optional[Dict[str, Any]]:
        """
        Get task status
        
        Args:
            task_id: Task ID
        
        Returns:
            Task status dictionary
        """
        task = self.tasks.get(task_id)
        if task is None:
            return None
        
        return {
            "id": task.id,
            "status": task.status.value,
            "retries": task.retries,
            "max_retries": task.max_retries,
            "created_at": task.created_at.isoformat(),
            "started_at": task.started_at.isoformat() if task.started_at else None,
            "completed_at": task.completed_at.isoformat() if task.completed_at else None,
            "error": task.error
        }
    
    def get_queue_stats(self) -> Dict[str, Any]:
        """
        Get queue statistics
        
        Returns:
            Queue statistics
        """
        pending = sum(1 for t in self.tasks.values() if t.status == TaskStatus.PENDING)
        processing = sum(1 for t in self.tasks.values() if t.status == TaskStatus.PROCESSING)
        completed = sum(1 for t in self.tasks.values() if t.status == TaskStatus.COMPLETED)
        failed = sum(1 for t in self.tasks.values() if t.status == TaskStatus.FAILED)
        
        return {
            "queue_size": self.queue.qsize(),
            "pending": pending,
            "processing": processing,
            "completed": completed,
            "failed": failed,
            "total": len(self.tasks),
            "workers": len(self.workers),
            "running": self.running
        }


# Global queue instance (The Perimeter: Clear jurisdiction)
_queue_system: Optional[QueueSystem] = None


def get_queue_system(max_workers: int = 10) -> QueueSystem:
    """
    Get or create queue system
    
    Args:
        max_workers: Maximum concurrent workers
    
    Returns:
        QueueSystem instance
    """
    global _queue_system
    
    if _queue_system is None:
        _queue_system = QueueSystem(max_workers=max_workers)
    
    return _queue_system


def queued(max_retries: int = 3):
    """
    Decorator for queuing function execution
    
    Usage:
        @queued(max_retries=3)
        def background_task():
            # Background work
            return result
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            queue = get_queue_system()
            task_id = await queue.enqueue(func, *args, max_retries=max_retries, **kwargs)
            return task_id
        return wrapper
    return decorator
