import type { ScanResponse, ScanStrategy } from "@/types";

export function getScanStrategy(results: ScanResponse): ScanStrategy {
  const hasVTFlags =
    results.vt_analysis?.malicious > 0 || results.vt_analysis?.suspicious > 0;
  const isAIDangerous =
    results.verdict === "Dangerous" || results.verdict === "Suspicious";
  const isSkipped = results.vt_analysis?.status === "skipped";

  if (hasVTFlags) {
    return {
      label: "High Alert",
      severity: "high",
      icon: "TriangleAlert",
      description:
        "Confirmed threat. This URL is blacklisted in global security databases.",
    };
  }

  if (!isSkipped && isAIDangerous) {
    return {
      label: "Heuristic Warning",
      severity: "medium",
      icon: "ShieldQuestionMark",
      description:
        "No known record found, but the URL structure mimics phishing patterns.",
    };
  }

  if (isSkipped && isAIDangerous) {
    return {
      label: "Social Engineering Alert",
      severity: "medium",
      icon: "MessageSquareWarning",
      description:
        "No suspicious links detected, but the message language suggests fraud or impersonation.",
    };
  }

  return {
    label: "Clear",
    severity: "safe",
    icon: "ShieldCheck",
    description:
      "No technical or behavioral threats were detected in this content.",
  };
}
