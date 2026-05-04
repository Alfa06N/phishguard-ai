export interface ScanResponse {
  verdict: string;
  score: number;
  ai_analysis: {
    technical_red_flags: string[];
    psychological_triggers: string[];
    verdict: string;
    risk_score: number;
  };
  vt_analysis: {
    malicious: number;
    suspicious: number;
    harmless: number;
    status: string;
    reason?: string;
  };
  domain_info: string | null;
  threats: string[];
}

export interface ScanStrategy {
  label: string;
  severity: "low" | "medium" | "high" | "safe";
  icon: string;
  description: string;
}

export interface ApiError {
  status: number;
  message: string;
  type: string;
}
