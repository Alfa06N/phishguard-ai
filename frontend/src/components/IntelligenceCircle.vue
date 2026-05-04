<script setup lang="ts">
import { motion } from "motion-v";
import { computed } from "vue";
const props = defineProps<{
  value: number;
  label: string;
  colorClass: string;
  glowRGB: string;
  bgClass: string;
}>();

const glowStyle = computed(() => ({
  "--glow-color": props.glowRGB,
}));
</script>
<!-- IntelligenceCircle.vue -->
<template>
  <div class="flex flex-col items-center gap-6 group" :style="glowStyle">
    <div class="relative h-32 w-32 md:h-40 md:w-40">
      <!-- Filtro de resplandor dinámico -->
      <svg
        class="h-full w-full -rotate-90 drop-shadow-[0_0_15px_rgba(var(--glow-color),0.3)]"
        viewBox="0 0 36 36"
      >
        <circle
          cx="18"
          cy="18"
          r="16"
          fill="none"
          class="stroke-zinc-800/40"
          stroke-width="2.5"
        />
        <motion.circle
          cx="18"
          cy="18"
          r="16"
          fill="none"
          :class="colorClass"
          stroke-width="2.5"
          stroke-linecap="round"
          :initial="{ pathLength: 0 }"
          :animate="{ pathLength: value / 100 }"
          :transition="{ duration: 2, ease: [0.4, 0, 0.2, 1] }"
        />
      </svg>

      <!-- Counter Central -->
      <div class="absolute inset-0 flex flex-col items-center justify-center">
        <span class="text-3xl font-black font-mono tracking-tighter">{{
          value
        }}</span>
        <span class="text-[10px] opacity-30 font-bold uppercase tracking-widest"
          >Score</span
        >
      </div>
    </div>

    <!-- Label con mayor tracking -->
    <div class="text-center space-y-1">
      <span
        :class="['text-xs font-black uppercase tracking-[0.4em]', colorClass]"
      >
        {{ label }}
      </span>
      <div
        class="h-1 w-8 mx-auto rounded-full opacity-20"
        :class="bgClass"
      ></div>
    </div>
  </div>
</template>
