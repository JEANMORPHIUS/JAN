# Troubleshooting FAQ

**Common issues and solutions for JAN Studio in the classroom**

---

## General Issues

### Q: The interface won't load

**A:** Check these steps:
1. Is the service running? `sudo systemctl status jan-studio-kids`
2. Can you access `http://localhost:8000`?
3. Check logs: `sudo journalctl -u jan-studio-kids -n 50`
4. Try restarting: `sudo systemctl restart jan-studio-kids`

---

### Q: Content generation is slow

**A:** This is normal! Generation takes 30-60 seconds. If it's taking longer:
1. Check CPU usage: `top`
2. Check if models are loaded: `curl http://localhost:8000/api/health`
3. Close other applications
4. Reduce `max_length` parameter

---

### Q: Generated content is weird or doesn't make sense

**A:** This is normal, especially with first attempts:
1. Personas need refinement
2. Prompts need to be more specific
3. This is a learning opportunity - discuss with students
4. Encourage iteration and improvement

---

### Q: Students can't access from their devices

**A:** Check network setup:
1. Find Pi IP: `hostname -I`
2. Ensure Pi and student devices are on same network
3. Check firewall: `sudo ufw status`
4. Try accessing from Pi first: `http://localhost:8000`
5. Then try from student device: `http://<pi-ip>:8000`

---

## Technical Issues

### Q: Out of memory errors

**A:** 
1. Check memory: `free -h`
2. Enable swap if needed
3. Close other applications
4. Restart service: `sudo systemctl restart jan-studio-kids`

---

### Q: Models won't download

**A:**
1. Check internet connection
2. Check disk space: `df -h`
3. Check model directory permissions
4. Try manual download (see setup guide)

---

### Q: Service keeps crashing

**A:**
1. Check logs: `sudo journalctl -u jan-studio-kids -n 100`
2. Check system resources: `htop`
3. Check for errors in logs
4. Try increasing memory limit in service file
5. Restart Pi if needed

---

## Student Issues

### Q: Student says "nothing is happening"

**A:**
1. Check if they clicked the button
2. Check if generation is in progress (loading indicator)
3. Check browser console for errors
4. Try refreshing the page
5. Check if service is running

---

### Q: Student can't hear read-aloud

**A:**
1. Check browser supports speech synthesis (Chrome/Edge work best)
2. Check device volume
3. Check browser permissions
4. Try different browser

---

### Q: Student's work disappeared

**A:**
1. Check browser localStorage (data is stored locally)
2. Check if they're on the same device/browser
3. Encourage saving to USB regularly
4. Consider implementing server-side storage (future feature)

---

### Q: Voice input doesn't work

**A:**
1. Check browser supports speech recognition (Chrome/Edge work best)
2. Check microphone permissions
3. Check if microphone is working
4. Try typing instead

---

## Classroom Management

### Q: Multiple students want to use it at once

**A:**
- Current version supports multiple users
- Each student's data is stored in their browser
- Consider having students take turns if it's slow
- Future: Multiple Pi setup or cloud version

---

### Q: Students are creating inappropriate content

**A:**
- Content is filtered for age-appropriateness
- Discuss appropriate use with students
- Review personas and rules
- Monitor student work
- Use as teaching moment about responsible AI use

---

### Q: How do I save student work?

**A:**
- Students can save to USB using the "Save to USB" button
- Files download to Downloads folder
- Can be copied to USB drive
- Consider creating a shared folder for class work

---

## Performance

### Q: Pi is running slow

**A:**
1. Check CPU temperature: `vcgencmd measure_temp`
2. Check memory usage: `free -h`
3. Close other applications
4. Consider adding cooling (fan/heatsink)
5. Restart Pi if needed

---

### Q: Generation takes too long

**A:**
- Normal: 30-60 seconds
- If longer: Check system resources
- Reduce `max_length` parameter
- Close other applications
- Consider this a teaching moment about AI processing time

---

## Getting Help

### Logs to Check

```bash
# Service logs
sudo journalctl -u jan-studio-kids -n 100

# System logs
dmesg | tail

# Resource usage
htop
free -h
df -h
```

### Information to Provide

When asking for help, provide:
1. Error messages from logs
2. Steps to reproduce
3. System information: `uname -a`
4. Service status: `sudo systemctl status jan-studio-kids`
5. What you've already tried

---

## Prevention Tips

1. **Regular restarts:** Restart Pi weekly
2. **Monitor resources:** Check memory/CPU regularly
3. **Backup:** Keep backups of student work
4. **Updates:** Keep system updated (optional)
5. **Documentation:** Keep setup notes

---

**FAQ Version:** 1.0  
**Last Updated:** 2025-01-27

