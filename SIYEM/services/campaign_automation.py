"""
CAMPAIGN AUTOMATION SYSTEM
Email Integration + Social Media Scheduling + Response Tracking

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

CAMPAIGN AUTOMATION:
- Email integration with contact list
- Social media scheduling (Later.com, Metricool, Publer, Buffer)
- Response tracking and analytics
- Campaign performance monitoring

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X.
"""

import os
import json
import csv
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from pathlib import Path
import logging
import sqlite3
from contextlib import contextmanager
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email.utils import formataddr

logger = logging.getLogger(__name__)


@contextmanager
def get_campaign_db():
    """Context manager for campaign database connections."""
    DB_PATH = Path(__file__).parent.parent / "data" / "campaign_automation.db"
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_campaign_db():
    """Initialize the campaign automation database."""
    with get_campaign_db() as conn:
        cursor = conn.cursor()
        
        # Contact list table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                name TEXT,
                organization TEXT,
                role TEXT,
                category TEXT,  -- media, regulatory, school, etc.
                tags TEXT,  -- JSON array of tags
                status TEXT DEFAULT 'active',  -- active, unsubscribed, bounced
                source TEXT,  -- where contact came from
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Email campaigns table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS email_campaigns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                campaign_name TEXT NOT NULL,
                subject TEXT NOT NULL,
                body_html TEXT,
                body_text TEXT,
                sender_email TEXT NOT NULL,
                sender_name TEXT,
                status TEXT DEFAULT 'draft',  -- draft, scheduled, sent, paused
                scheduled_at TIMESTAMP,
                sent_at TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Email sends table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS email_sends (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                campaign_id INTEGER NOT NULL,
                contact_id INTEGER NOT NULL,
                email TEXT NOT NULL,
                status TEXT DEFAULT 'pending',  -- pending, sent, delivered, bounced, opened, clicked
                sent_at TIMESTAMP,
                delivered_at TIMESTAMP,
                opened_at TIMESTAMP,
                clicked_at TIMESTAMP,
                bounce_reason TEXT,
                error_message TEXT,
                FOREIGN KEY (campaign_id) REFERENCES email_campaigns(id),
                FOREIGN KEY (contact_id) REFERENCES contacts(id)
            )
        """)
        
        # Social media posts table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS social_posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,  -- twitter, instagram, linkedin, facebook, tiktok
                content TEXT NOT NULL,
                media_url TEXT,
                scheduled_at TIMESTAMP,
                posted_at TIMESTAMP,
                status TEXT DEFAULT 'draft',  -- draft, scheduled, posted, failed
                post_id TEXT,  -- Platform post ID after posting
                engagement_data TEXT,  -- JSON: likes, comments, shares, etc.
                error_message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Social media scheduling table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS social_schedules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                scheduler TEXT NOT NULL,  -- later, metricool, publer, buffer
                platform TEXT NOT NULL,
                post_id INTEGER NOT NULL,
                scheduler_post_id TEXT,  -- ID from scheduler service
                status TEXT DEFAULT 'pending',  -- pending, scheduled, posted, failed
                scheduled_at TIMESTAMP,
                posted_at TIMESTAMP,
                error_message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (post_id) REFERENCES social_posts(id)
            )
        """)
        
        # Response tracking table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS responses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contact_id INTEGER,
                email TEXT,
                source TEXT,  -- email, social, website, etc.
                response_type TEXT,  -- reply, click, signup, etc.
                content TEXT,
                metadata TEXT,  -- JSON
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (contact_id) REFERENCES contacts(id)
            )
        """)
        
        # Campaign analytics table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS campaign_analytics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                campaign_id INTEGER,
                campaign_type TEXT,  -- email, social, combined
                metric_date DATE NOT NULL,
                metric_name TEXT NOT NULL,  -- sent, delivered, opened, clicked, engaged, etc.
                metric_value INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (campaign_id) REFERENCES email_campaigns(id),
                UNIQUE(campaign_id, metric_date, metric_name)
            )
        """)
        
        # Create indexes
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_contacts_email ON contacts(email)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_contacts_category ON contacts(category)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_email_sends_campaign ON email_sends(campaign_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_email_sends_contact ON email_sends(contact_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_social_posts_platform ON social_posts(platform)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_social_posts_status ON social_posts(status)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_responses_contact ON responses(contact_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_analytics_campaign_date ON campaign_analytics(campaign_id, metric_date)")
        
        conn.commit()


# Initialize database on import
init_campaign_db()


class ContactManager:
    """Manage contact list for campaigns."""
    
    @staticmethod
    def add_contact(
        email: str,
        name: Optional[str] = None,
        organization: Optional[str] = None,
        role: Optional[str] = None,
        category: Optional[str] = None,
        tags: Optional[List[str]] = None,
        source: Optional[str] = None,
        notes: Optional[str] = None
    ) -> Dict[str, Any]:
        """Add a contact to the database."""
        with get_campaign_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO contacts
                (email, name, organization, role, category, tags, source, notes, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                email,
                name,
                organization,
                role,
                category,
                json.dumps(tags or []),
                source,
                notes,
                datetime.now()
            ))
            conn.commit()
            
            return {
                "id": cursor.lastrowid,
                "email": email,
                "name": name,
                "status": "added"
            }
    
    @staticmethod
    def import_contacts_from_csv(file_path: str) -> Dict[str, Any]:
        """Import contacts from CSV file."""
        contacts_added = 0
        contacts_updated = 0
        errors = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        ContactManager.add_contact(
                            email=row.get('email', '').strip(),
                            name=row.get('name', '').strip() or None,
                            organization=row.get('organization', '').strip() or None,
                            role=row.get('role', '').strip() or None,
                            category=row.get('category', '').strip() or None,
                            tags=row.get('tags', '').split(',') if row.get('tags') else None,
                            source=row.get('source', 'csv_import').strip() or None,
                            notes=row.get('notes', '').strip() or None
                        )
                        contacts_added += 1
                    except Exception as e:
                        errors.append(f"Error importing {row.get('email', 'unknown')}: {str(e)}")
            
            return {
                "status": "success",
                "contacts_added": contacts_added,
                "errors": errors
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "contacts_added": contacts_added
            }
    
    @staticmethod
    def get_contacts(
        category: Optional[str] = None,
        status: str = "active",
        tags: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """Get contacts matching criteria."""
        with get_campaign_db() as conn:
            cursor = conn.cursor()
            
            query = "SELECT * FROM contacts WHERE status = ?"
            params = [status]
            
            if category:
                query += " AND category = ?"
                params.append(category)
            
            if tags:
                # Filter by tags (JSON array contains)
                tag_conditions = []
                for tag in tags:
                    tag_conditions.append("tags LIKE ?")
                    params.append(f'%"{tag}"%')
                if tag_conditions:
                    query += " AND (" + " OR ".join(tag_conditions) + ")"
            
            cursor.execute(query, params)
            rows = cursor.fetchall()
            
            contacts = []
            for row in rows:
                contact = dict(row)
                if contact.get("tags"):
                    contact["tags"] = json.loads(contact["tags"])
                contacts.append(contact)
            
            return contacts


class EmailCampaign:
    """Email campaign management."""
    
    def __init__(
        self,
        smtp_server: Optional[str] = None,
        smtp_port: Optional[int] = None,
        smtp_user: Optional[str] = None,
        smtp_password: Optional[str] = None
    ):
        self.smtp_server = smtp_server or os.getenv("SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = smtp_port or int(os.getenv("SMTP_PORT", "587"))
        self.smtp_user = smtp_user or os.getenv("SMTP_USER")
        self.smtp_password = smtp_password or os.getenv("SMTP_PASSWORD")
    
    def create_campaign(
        self,
        campaign_name: str,
        subject: str,
        body_html: str,
        body_text: Optional[str] = None,
        sender_email: str = None,
        sender_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create an email campaign."""
        with get_campaign_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO email_campaigns
                (campaign_name, subject, body_html, body_text, sender_email, sender_name)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                campaign_name,
                subject,
                body_html,
                body_text or self._html_to_text(body_html),
                sender_email or self.smtp_user,
                sender_name
            ))
            conn.commit()
            
            return {
                "id": cursor.lastrowid,
                "campaign_name": campaign_name,
                "status": "draft"
            }
    
    def send_campaign(
        self,
        campaign_id: int,
        contact_ids: Optional[List[int]] = None,
        categories: Optional[List[str]] = None,
        tags: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Send email campaign to contacts."""
        # Get campaign
        with get_campaign_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM email_campaigns WHERE id = ?", (campaign_id,))
            campaign = dict(cursor.fetchone())
        
        # Get contacts
        if contact_ids:
            contacts = [ContactManager.get_contacts()[c-1] for c in contact_ids if c <= len(ContactManager.get_contacts())]
        else:
            contacts = ContactManager.get_contacts(category=categories[0] if categories else None, tags=tags)
        
        # Send emails
        sent = 0
        failed = 0
        errors = []
        
        for contact in contacts:
            try:
                self._send_email(
                    to_email=contact["email"],
                    to_name=contact.get("name"),
                    subject=campaign["subject"],
                    body_html=campaign["body_html"],
                    body_text=campaign["body_text"],
                    sender_email=campaign["sender_email"],
                    sender_name=campaign["sender_name"]
                )
                
                # Record send
                with get_campaign_db() as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        INSERT INTO email_sends
                        (campaign_id, contact_id, email, status, sent_at)
                        VALUES (?, ?, ?, 'sent', ?)
                    """, (campaign_id, contact["id"], contact["email"], datetime.now()))
                    conn.commit()
                
                sent += 1
            except Exception as e:
                failed += 1
                errors.append(f"{contact['email']}: {str(e)}")
                
                # Record failure
                with get_campaign_db() as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        INSERT INTO email_sends
                        (campaign_id, contact_id, email, status, error_message, sent_at)
                        VALUES (?, ?, ?, 'failed', ?, ?)
                    """, (campaign_id, contact.get("id"), contact["email"], str(e), datetime.now()))
                    conn.commit()
        
        # Update campaign status
        with get_campaign_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE email_campaigns
                SET status = 'sent', sent_at = ?, updated_at = ?
                WHERE id = ?
            """, (datetime.now(), datetime.now(), campaign_id))
            conn.commit()
        
        return {
            "campaign_id": campaign_id,
            "sent": sent,
            "failed": failed,
            "errors": errors
        }
    
    def _send_email(
        self,
        to_email: str,
        to_name: Optional[str],
        subject: str,
        body_html: str,
        body_text: str,
        sender_email: str,
        sender_name: Optional[str]
    ):
        """Send individual email."""
        if not self.smtp_user or not self.smtp_password:
            raise ValueError("SMTP credentials not configured")
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = formataddr((sender_name or "JAN MUHARREM", sender_email))
        msg['To'] = formataddr((to_name or "", to_email)) if to_name else to_email
        
        part1 = MIMEText(body_text, 'plain')
        part2 = MIMEText(body_html, 'html')
        
        msg.attach(part1)
        msg.attach(part2)
        
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            server.send_message(msg)
    
    def _html_to_text(self, html: str) -> str:
        """Convert HTML to plain text (basic)."""
        import re
        text = re.sub('<[^<]+?>', '', html)
        text = text.replace('&nbsp;', ' ')
        text = text.replace('&amp;', '&')
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')
        return text.strip()


class SocialMediaScheduler:
    """Social media scheduling and posting."""
    
    def __init__(self):
        self.schedulers = {
            "later": self._export_to_later,
            "metricool": self._export_to_metricool,
            "publer": self._export_to_publer,
            "buffer": self._export_to_buffer
        }
    
    def create_post(
        self,
        platform: str,
        content: str,
        media_url: Optional[str] = None,
        scheduled_at: Optional[datetime] = None
    ) -> Dict[str, Any]:
        """Create a social media post."""
        with get_campaign_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO social_posts
                (platform, content, media_url, scheduled_at, status)
                VALUES (?, ?, ?, ?, ?)
            """, (
                platform,
                content,
                media_url,
                scheduled_at,
                "scheduled" if scheduled_at else "draft"
            ))
            conn.commit()
            
            return {
                "id": cursor.lastrowid,
                "platform": platform,
                "status": "scheduled" if scheduled_at else "draft"
            }
    
    def export_to_scheduler(
        self,
        scheduler: str,
        post_ids: Optional[List[int]] = None,
        platform: Optional[str] = None
    ) -> Dict[str, Any]:
        """Export posts to scheduling service."""
        # Get posts
        with get_campaign_db() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM social_posts WHERE status IN ('draft', 'scheduled')"
            params = []
            
            if post_ids:
                query += " AND id IN (" + ",".join(["?"] * len(post_ids)) + ")"
                params.extend(post_ids)
            
            if platform:
                query += " AND platform = ?"
                params.append(platform)
            
            cursor.execute(query, params)
            posts = [dict(row) for row in cursor.fetchall()]
        
        # Export to scheduler
        if scheduler not in self.schedulers:
            return {"status": "error", "error": f"Unknown scheduler: {scheduler}"}
        
        export_func = self.schedulers[scheduler]
        return export_func(posts)
    
    def _export_to_later(self, posts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Export to Later.com CSV format."""
        csv_data = []
        for post in posts:
            csv_data.append({
                "Text": post["content"],
                "Media": post.get("media_url", ""),
                "Link": "",
                "Date": post.get("scheduled_at", "").strftime("%Y-%m-%d %H:%M:%S") if post.get("scheduled_at") else "",
                "Platform": post["platform"].upper()
            })
        
        return {
            "status": "success",
            "format": "later_csv",
            "posts": csv_data,
            "count": len(csv_data)
        }
    
    def _export_to_metricool(self, posts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Export to Metricool CSV format."""
        csv_data = []
        for post in posts:
            csv_data.append({
                "Content": post["content"],
                "Image URL": post.get("media_url", ""),
                "Scheduled Date": post.get("scheduled_at", "").strftime("%Y-%m-%d %H:%M:%S") if post.get("scheduled_at") else "",
                "Network": post["platform"]
            })
        
        return {
            "status": "success",
            "format": "metricool_csv",
            "posts": csv_data,
            "count": len(csv_data)
        }
    
    def _export_to_publer(self, posts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Export to Publer CSV format."""
        csv_data = []
        for post in posts:
            csv_data.append({
                "message": post["content"],
                "media": post.get("media_url", ""),
                "schedule": post.get("scheduled_at", "").strftime("%Y-%m-%d %H:%M:%S") if post.get("scheduled_at") else "",
                "network": post["platform"]
            })
        
        return {
            "status": "success",
            "format": "publer_csv",
            "posts": csv_data,
            "count": len(csv_data)
        }
    
    def _export_to_buffer(self, posts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Export to Buffer CSV format."""
        csv_data = []
        for post in posts:
            csv_data.append({
                "text": post["content"],
                "media": post.get("media_url", ""),
                "scheduled_at": post.get("scheduled_at", "").strftime("%Y-%m-%d %H:%M:%S") if post.get("scheduled_at") else "",
                "profile": post["platform"]
            })
        
        return {
            "status": "success",
            "format": "buffer_csv",
            "posts": csv_data,
            "count": len(csv_data)
        }


class ResponseTracker:
    """Track campaign responses and engagement."""
    
    @staticmethod
    def record_response(
        email: Optional[str] = None,
        contact_id: Optional[int] = None,
        source: str = "email",
        response_type: str = "reply",
        content: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Record a response."""
        with get_campaign_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO responses
                (contact_id, email, source, response_type, content, metadata)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                contact_id,
                email,
                source,
                response_type,
                content,
                json.dumps(metadata or {})
            ))
            conn.commit()
            
            return {
                "id": cursor.lastrowid,
                "status": "recorded"
            }
    
    @staticmethod
    def get_responses(
        contact_id: Optional[int] = None,
        response_type: Optional[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[Dict[str, Any]]:
        """Get responses matching criteria."""
        with get_campaign_db() as conn:
            cursor = conn.cursor()
            
            query = "SELECT * FROM responses WHERE 1=1"
            params = []
            
            if contact_id:
                query += " AND contact_id = ?"
                params.append(contact_id)
            
            if response_type:
                query += " AND response_type = ?"
                params.append(response_type)
            
            if start_date:
                query += " AND created_at >= ?"
                params.append(start_date)
            
            if end_date:
                query += " AND created_at <= ?"
                params.append(end_date)
            
            query += " ORDER BY created_at DESC"
            
            cursor.execute(query, params)
            rows = cursor.fetchall()
            
            responses = []
            for row in rows:
                response = dict(row)
                if response.get("metadata"):
                    response["metadata"] = json.loads(response["metadata"])
                responses.append(response)
            
            return responses


class CampaignAnalytics:
    """Campaign analytics and reporting."""
    
    @staticmethod
    def get_campaign_stats(campaign_id: int) -> Dict[str, Any]:
        """Get comprehensive campaign statistics."""
        with get_campaign_db() as conn:
            cursor = conn.cursor()
            
            # Email sends stats
            cursor.execute("""
                SELECT 
                    COUNT(*) as total,
                    SUM(CASE WHEN status = 'sent' THEN 1 ELSE 0 END) as sent,
                    SUM(CASE WHEN status = 'delivered' THEN 1 ELSE 0 END) as delivered,
                    SUM(CASE WHEN status = 'opened' THEN 1 ELSE 0 END) as opened,
                    SUM(CASE WHEN status = 'clicked' THEN 1 ELSE 0 END) as clicked,
                    SUM(CASE WHEN status = 'bounced' THEN 1 ELSE 0 END) as bounced
                FROM email_sends
                WHERE campaign_id = ?
            """, (campaign_id,))
            
            email_stats = dict(cursor.fetchone())
            
            # Response stats
            cursor.execute("""
                SELECT COUNT(*) as total_responses
                FROM responses r
                JOIN email_sends es ON r.contact_id = es.contact_id
                WHERE es.campaign_id = ?
            """, (campaign_id,))
            
            response_stats = dict(cursor.fetchone())
            
            return {
                "campaign_id": campaign_id,
                "email_stats": email_stats,
                "response_stats": response_stats,
                "open_rate": (email_stats["opened"] / email_stats["sent"] * 100) if email_stats["sent"] > 0 else 0,
                "click_rate": (email_stats["clicked"] / email_stats["sent"] * 100) if email_stats["sent"] > 0 else 0,
                "bounce_rate": (email_stats["bounced"] / email_stats["sent"] * 100) if email_stats["sent"] > 0 else 0
            }
    
    @staticmethod
    def update_analytics(
        campaign_id: int,
        metric_date: datetime,
        metrics: Dict[str, int]
    ):
        """Update campaign analytics."""
        with get_campaign_db() as conn:
            cursor = conn.cursor()
            for metric_name, metric_value in metrics.items():
                cursor.execute("""
                    INSERT OR REPLACE INTO campaign_analytics
                    (campaign_id, campaign_type, metric_date, metric_name, metric_value)
                    VALUES (?, 'email', ?, ?, ?)
                """, (campaign_id, metric_date.date(), metric_name, metric_value))
            conn.commit()
