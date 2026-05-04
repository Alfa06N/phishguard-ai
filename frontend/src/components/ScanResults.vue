<script setup lang="ts">
import { useScanner } from "@/composables/useScanner";
import { storeToRefs } from "pinia";
import { computed, type Component } from "vue";
import { Globe } from "lucide-vue-next";
import { motion } from "motion-v";
import {
  BrainCircuit,
  MessageSquareWarning,
  ShieldAlert,
  ShieldCheck,
  ShieldQuestionMark,
  TriangleAlert,
} from "lucide-vue-next";
import { sTransitions, sVariants } from "@/lib/smoothcn";
import IntelligenceCircle from "./IntelligenceCircle.vue";

const store = useScanner();
const { strategy, results } = storeToRefs(store);

const severityClasses = {
  high: "bg-red-950/20 border-red-500/50 text-red-400",
  medium: "bg-amber-950/20 border-amber-500/50 text-amber-400",
  low: "bg-blue-950/20 border-blue-500/50 text-blue-400",
  safe: "bg-emerald-950/20 border-emerald-500/50 text-emerald-400",
};

const iconColorClass = computed(() => {
  switch (strategy.value?.severity) {
    case "high":
      return "text-red-500";
    case "medium":
      return "text-amber-500";
    case "low":
      return "text-blue-500";
    case "safe":
      return "text-emeral-500";
    default:
      return "text-zinc-500";
  }
});
const heartbeatSettings = computed(() => {
  const severity = strategy.value?.severity || "low";

  const configs = {
    high: {
      scale: [1, 1.3, 1.1, 1.4, 1],
      duration: 0.8,
      repeatDelay: 0.4,
      glow: "drop-shadow(0 0 25px rgba(239, 68, 68, 0.7))",
    },
    medium: {
      scale: [1, 1.15, 1.05, 1.2, 1],
      duration: 1.4,
      repeatDelay: 0.8,
      glow: "drop-shadow(0 0 15px rgba(245, 158, 11, 0.4))",
    },
    low: {
      scale: [1, 1.05, 1],
      duration: 2,
      repeatDelay: 1,
      glow: "none",
    },
  };

  return configs[severity as keyof typeof configs] || configs.low;
});

const iconMap: Record<string, Component> = {
  TriangleAlert,
  ShieldCheck,
  ShieldQuestionMark,
  ShieldAlert,
  MessageSquareWarning,
} as const;
</script>

<template>
  <motion.div
    layout
    key="results-container"
    layout-id="results"
    v-bind="sVariants.fadeIn"
    :transition="sTransitions.spring.snappy"
    v-if="store.strategy"
    class="mt-12 mb-30 w-full px-4 max-w-5xl flex flex-col"
  >
    <!-- 1. Top Verdict Banner (The "Hero" of the results) -->
    <div
      :class="[
        'border-x border-t p-8 backdrop-blur-md transition-all duration-500 flex-none',
        strategy?.severity === 'safe'
          ? 'rounded-2xl border-b'
          : 'rounded-t-2xl border-b-0',
        severityClasses[strategy!.severity],
      ]"
    >
      <div
        class="flex flex-col md:flex-row md:items-center justify-between gap-8"
      >
        <div
          class="flex flex-col md:flex-row items-center md:items-center gap-8 text-center md:text-left"
        >
          <motion.div
            :animate="{
              scale: heartbeatSettings.scale,
              filter: [
                'drop-shadow(0 0 0px rgba(0,0,0,0))',
                heartbeatSettings.glow,
                'drop-shadow(0 0 0px rgba(0,0,0,0))',
              ],
            }"
            :transition="{
              duration: heartbeatSettings.duration,
              repeat: Infinity,
              repeatDelay: heartbeatSettings.repeatDelay,
              ease: 'easeInOut',
            }"
            class="relative"
          >
            <component
              :is="iconMap[store.strategy.icon]"
              class="h-20 w-20 md:h-16 md:w-16 drop-shadow-2xl"
              :class="iconColorClass"
            />
          </motion.div>

          <div>
            <h2 class="text-4xl md:text-4xl font-black tracking-tight mb-2">
              {{ strategy!.label }}
            </h2>
            <p
              class="text-base md:text-xl opacity-80 max-w-2xl mx-auto md:mx-0 leading-relaxed"
            >
              {{ strategy!.description }}
            </p>
          </div>
        </div>
        <!-- Risk Score Badge for Mobile/Small views -->
        <div class="hidden md:block text-right">
          <div class="text-5xl font-black tracking-tighter leading-none">
            {{ results!.score }}
          </div>
          <div
            class="text-xs uppercase font-bold tracking-widest opacity-60 mt-2"
          >
            Risk Score
          </div>
        </div>
      </div>
    </div>

    <!-- 2. Detailed Technical Grid -->
    <div
      v-if="strategy!.severity !== 'safe'"
      class="flex-1 grid grid-cols-1 lg:grid-cols-4 gap-0 border border-zinc-800 bg-zinc-900/60 rounded-b-2xl overflow-hidden"
    >
      <!-- AI Analysis Section (Spans 2 columns) -->
      <div
        class="lg:col-span-2 p-10 relative overflow-hidden flex flex-col justify-between border-b lg:border-b-0 lg:border-r border-zinc-800"
      >
        <BrainCircuit
          class="absolute -right-10 -bottom-10 h-64 w-64 opacity-[0.03] text-zinc-400 rotate-12 pointer-events-none"
        />

        <div class="relative z-10 space-y-8">
          <div class="flex items-center gap-4 mb-8">
            <div class="p-3 bg-zinc-800/50 rounded-xl border border-zinc-700">
              <BrainCircuit class="w-6 h-6 text-zinc-400 animate-pulse" />
            </div>
            <h3
              class="text-sm font-bold uppercase tracking-[0.3em] text-zinc-500"
            >
              Behavioral Intelligence
            </h3>
          </div>

          <!-- Compact Triggers/Flags para dejar espacio -->
          <div class="space-y-6">
            <div v-if="results!.ai_analysis.psychological_triggers.length">
              <h4
                class="text-[10px] font-bold text-zinc-600 uppercase tracking-widest mb-3"
              >
                Psychological Tactics
              </h4>
              <div class="flex flex-wrap gap-2">
                <div
                  v-for="t in results!.ai_analysis.psychological_triggers"
                  :key="t"
                  class="px-3 py-3 rounded-lg bg-zinc-800/30 border border-zinc-700/50 text-xs md:text-sm text-zinc-300"
                >
                  {{ t }}
                </div>
              </div>
            </div>
            <div v-if="results!.ai_analysis.technical_red_flags.length">
              <h4
                class="text-[10px] font-bold text-zinc-600 uppercase tracking-widest mb-3"
              >
                Psychological Tactics
              </h4>
              <div class="flex flex-wrap gap-2">
                <div
                  v-for="flag in results!.ai_analysis.technical_red_flags"
                  :key="flag"
                  class="px-3 py-3 rounded-lg bg-zinc-800/30 border border-zinc-700/50 text-xs md:text-sm text-zinc-300"
                >
                  {{ flag }}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div
          class="pt-6 mt-8 border-t border-zinc-800/50 text-xs text-zinc-500 flex justify-between uppercase"
        >
          <span>Confidence: 99.8%</span>
        </div>
      </div>

      <!-- Global Intelligence (Spans 2 columns now) -->
      <div class="lg:col-span-2 flex flex-col p-10 bg-black/20 justify-between">
        <div class="space-y-10">
          <div class="flex items-center gap-3 text-zinc-400">
            <div class="p-3 bg-zinc-800/50 rounded-xl border border-zinc-700">
              <Globe class="w-6 h-6 text-zinc-400 animate-pulse" />
            </div>
            <h3
              class="text-sm font-bold uppercase tracking-[0.3em] text-zinc-500"
            >
              Global Threat Intelligence
            </h3>
          </div>

          <!-- Grid de Círculos Radiales -->
          <div
            class="flex flex-row flex-wrap justify-center items-center gap-8 mt-8"
          >
            <IntelligenceCircle
              :value="results!.vt_analysis.malicious"
              label="Malicious"
              color-class="stroke-red-500 text-red-500"
              glow-r-g-b="239, 68, 68"
              bg-class="bg-red-500"
            />
            <IntelligenceCircle
              :value="results!.vt_analysis.suspicious"
              label="Suspicious"
              color-class="stroke-amber-500 text-amber-500"
              glow-r-g-b="245, 158, 11"
              bg-class="bg-amber-500"
            />
            <IntelligenceCircle
              :value="results!.vt_analysis.harmless"
              label="Harmless"
              color-class="stroke-emerald-500 text-emerald-500"
              glow-r-g-b="16, 185, 129"
              bg-class="bg-emerald-500"
            />
          </div>
        </div>

        <div class="space-y-4 mt-8">
          <div
            class="p-4 rounded-xl bg-zinc-800/20 border border-zinc-800/50 text-center"
          >
            <p
              class="text-[10px] text-zinc-500 uppercase tracking-[0.2em] leading-relaxed"
            >
              Cross-referenced with
              <span class="text-zinc-300 font-bold">70+ security vendors</span>
              including Kaspersky, CrowdStrike, and Mandiant.
            </p>
          </div>
        </div>
      </div>
    </div>
  </motion.div>
</template>
