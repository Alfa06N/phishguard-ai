# PhishGuard AI

An AI-powered phishing detection tool that analyzes suspicious emails, URLs, and text content for social engineering threats in real time. It combines Google Gemini's language understanding with VirusTotal's global threat database to produce a comprehensive risk assessment.

---

## How it works

1. The user pastes an email body, URL, or any suspicious text into the input field.
2. The **FastAPI backend** sends the content to **Google Gemini 2.5 Flash**, which returns a structured JSON analysis including a risk score (0–100), psychological manipulation triggers, and technical red flags.
3. If a URL is detected in the content, it is also submitted to the **VirusTotal API** for a multi-engine malware/phishing verdict.
4. Both results are merged into a final verdict: **Safe**, **Suspicious**, or **Dangerous**.
5. The **Vue 3 frontend** displays the verdict, score, threat breakdown, and VirusTotal engine stats with animated transitions.

---

## Tech stack

| Layer         | Technology                                      |
| ------------- | ----------------------------------------------- |
| Frontend      | Vue 3, TypeScript, Vite, Tailwind CSS, Motion-V |
| Backend       | Python, FastAPI, Pydantic                       |
| AI            | Google Gemini 2.5 Flash (via `google-genai`)    |
| Threat Intel  | VirusTotal API v3                               |
| Rate limiting | slowapi                                         |

---

## Project structure

```
.
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/          # Utilities and exception helpers
│   │   ├── schemas/       # Pydantic request/response models
│   │   ├── services/
│   │   │   ├── ai_service.py   # Gemini integration
│   │   │   └── vt_service.py   # VirusTotal integration
│   │   └── main.py        # FastAPI app and routes
│   └── requirements.txt
└── frontend/
    └── src/
        ├── api/           # Axios client
        ├── components/    # UI components (Hero, ScanResults, etc.)
        ├── composables/   # useScanner store (Pinia)
        ├── types/         # TypeScript interfaces
        └── views/         # Dashboard view
```

---

## Getting started

### Prerequisites

- Python 3.11+
- Node.js 18+ and pnpm
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)
- A [VirusTotal API key](https://www.virustotal.com/gui/my-apikey)

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `backend/.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
VIRUSTOTAL_API_KEY=your_virustotal_api_key
```

Start the server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

### Frontend

```bash
cd frontend
pnpm install
pnpm dev
```

The app will be available at `http://localhost:5173`.

---

## API

### `POST /api/v1/scan`

Analyzes content for phishing threats.

**Request body**

```json
{ "content": "Your suspicious email or URL here" }
```

**Response**

```json
{
  "verdict": "Dangerous",
  "score": 92,
  "ai_analysis": {
    "risk_score": 92,
    "psychological_triggers": ["Urgency", "Fear"],
    "technical_red_flags": ["Suspicious TLD", "Mismatched domain"],
    "verdict": "Dangerous"
  },
  "vt_analysis": {
    "malicious": 5,
    "suspicious": 2,
    "harmless": 61,
    "status": "completed"
  },
  "domain_info": "http://example-phish.xyz",
  "threats": ["Suspicious TLD", "Urgency", "Fear"]
}
```

Rate limited to **5 requests per minute** per IP.

---

## Testing

Use the special keyword `test-phish` as the scan input to trigger a mock phishing response without consuming API quota.

---

Built with ❤️ by Alfa06N
