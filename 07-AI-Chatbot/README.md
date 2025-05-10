# LiveKit Assistant Setup Guide

## Quick Setup

1. **Create virtual environment and install packages**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
    
   
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. **Get required API keys**
   - **LiveKit credentials**:
     - Go to [LiveKit Cloud](https://cloud.livekit.io/)
     - Navigate to your project → Settings → API Keys
     - Create or copy existing API key and secret
     - Note your LiveKit URL (format: `wss://your-project.livekit.cloud`)

   - **Groq API Key**:
     - Go to [Groq Console](https://console.groq.com/)
     - Navigate to API Keys section
     - Create and copy your API key

3. **Set environment variables**
   ```bash
   # Windows
   LIVEKIT_URL=your_livekit_url
   LIVEKIT_API_KEY=your_livekit_api_key
   LIVEKIT_API_SECRET=your_livekit_api_secret
   GROQ_API_KEY=your_groq_api_key
   ```

4. **Run the assistant**
   ```bash
   python assistant.py download-files
   python assistant.py start
   ```

5. **Connect via LiveKit Playground**
   - Go to [LiveKit Playground](https://playground.livekit.io/)
   - Enter your LiveKit URL and a username
   - Click "Connect"
   - The assistant will automatically join and respond to voice/text


Need help? Check [LiveKit docs](https://docs.livekit.io/) or [Groq docs](https://console.groq.com/docs)