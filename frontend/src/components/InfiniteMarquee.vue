<script setup lang="ts">
import { sTransitions } from "@/lib/smoothcn";
import ExampleCard from "./ExampleCard.vue";
import { motion } from "motion-v";
const examples = [
  {
    text: "https://paypal-security-update.xyz",
    label: "Malicious URL",
    color: "text-red-400",
  },
  {
    text: "Your account will be suspended in 24h. Click here...",
    label: "Urgency Trigger",
    color: "text-amber-400",
  },
  {
    text: "Package delivery failed. Update your info at...",
    label: "Smishing",
    color: "text-red-400",
  },
  {
    text: "Verify your bank credentials for the new login",
    label: "Credential Theft",
    color: "text-orange-400",
  },
  {
    text: "https://google.com/search?q=security",
    label: "Safe URL",
    color: "text-emerald-400",
  },
  {
    text: "Your Netflix subscription has expired. Update your payment method at: https://net-flix-billing.cc",
    label: "Subscription Fraud",
    color: "text-red-500",
    severity: "high",
  },
  {
    text: "https://arnazon.com/deals/today-special-offers",
    label: "Typosquatting",
    color: "text-orange-500",
    severity: "high",
  },
  {
    text: "[FedEx]: Delivery failed. A redelivery fee of $1.99 is required. Visit: https://fedx-package.top",
    label: "Logistics Phishing",
    color: "text-red-500",
    severity: "high",
  },
  {
    text: "Annual Salary Review: Please sign the attached document via docusign-portal.net",
    label: "B2B Phishing",
    color: "text-amber-500",
    severity: "medium",
  },
  {
    text: "Claim your $ARB Airdrop before it's too late! Connect your wallet at: https://arbitrum-claim.io",
    label: "Crypto Drainer",
    color: "text-red-500",
    severity: "high",
  },
  {
    text: "https://github.com/nicolasalfaro/phishing-detector",
    label: "Safe / Developer",
    color: "text-emerald-500",
    severity: "low",
  },
  {
    text: "CRITICAL: Unauthorized login detected from Moscow, Russia. If this wasn't you, secure your account now.",
    label: "Fear Trigger",
    color: "text-amber-500",
    severity: "medium",
  },
  {
    text: "Urgent: Your tax refund is ready. Click here to provide your banking details: https://irs-gov-portal.online",
    label: "Government Impersonation",
    color: "text-red-500",
    severity: "high",
  },
  {
    text: "Attached: invoice_2024_scan_PDF.exe",
    label: "Malicious Attachment",
    color: "text-red-600",
    severity: "critical",
  },
  {
    text: "https://pnpm.io/installation",
    label: "Safe / Documentation",
    color: "text-emerald-500",
    severity: "low",
  },
];

const firstRow = examples.slice(0, 7);
const secondRow = examples.slice(7);
</script>

<template>
  <motion.div
    layout
    :transition="sTransitions.spring.snappy"
    class="relative w-full py-12 overflow-hidden bg-transparent mt-40 group"
  >
    <!-- Gradient Overlays para el efecto de "desaparecer" en los lados -->
    <div
      class="absolute inset-y-0 left-0 w-32 bg-gradient-to-r from-zinc-950 to-transparent z-10 pointer-events-none"
    ></div>
    <div
      class="absolute inset-y-0 right-0 w-32 bg-gradient-to-l from-zinc-950 to-transparent z-10 pointer-events-none"
    ></div>

    <!-- Fila 1: Movimiento a la Izquierda -->
    <div class="flex w-max animate-marquee-left pause-on-hover">
      <div v-for="i in 2" :key="i" class="flex gap-4 pr-4">
        <ExampleCard v-for="(item, idx) in firstRow" :key="idx" :item="item" />
      </div>
    </div>

    <!-- Fila 2: Movimiento a la Derecha -->
    <div class="flex w-max mt-4 animate-marquee-right pause-on-hover">
      <div v-for="i in 2" :key="i" class="flex gap-4 pr-4">
        <ExampleCard v-for="(item, idx) in secondRow" :key="idx" :item="item" />
      </div>
    </div>
  </motion.div>
</template>

<style scoped>
@keyframes marquee-left {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-50%);
  }
}

@keyframes marquee-right {
  0% {
    transform: translateX(-50%);
  }
  100% {
    transform: translateX(0);
  }
}

.animate-marquee-left {
  animation: marquee-left 50s linear infinite;
}

.animate-marquee-right {
  animation: marquee-right 60s linear infinite;
}

.pause-on-hover:hover {
  animation-play-state: paused;
}
</style>
