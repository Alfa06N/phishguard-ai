<script setup lang="ts">
import { motion } from "motion-v";
import { useScanner } from "@/composables/useScanner";
import { storeToRefs } from "pinia";
import { sTransitions, sVariants } from "@/lib/smoothcn";
import { BrainCircuit } from "lucide-vue-next";
import { watch, nextTick, ref } from "vue";

const store = useScanner();
const resultsAnchor = ref<HTMLElement | null>(null);
const { isScanning } = storeToRefs(store);

watch(isScanning, async (newVal) => {
  if (newVal) {
    await nextTick();

    resultsAnchor.value?.scrollIntoView({
      behavior: "smooth",
      block: "center",
    });
  }
});
</script>

<template>
  <motion.div
    v-if="isScanning"
    key="loading"
    layout-id="results"
    v-bind="sVariants.fadeIn"
    :transition="sTransitions.spring.snappy"
    class="w-full mb-30 border border-zinc-800 bg-zinc-900/40 rounded-2xl p-12 flex flex-col items-center justify-center min-h-[300px]"
  >
    <div class="relative mb-8" ref="resultsAnchor">
      <div
        class="absolute inset-0 rounded-full bg-blue-500/20 animate-ping"
      ></div>
      <BrainCircuit
        class="h-16 w-16 text-blue-500 animate-pulse relative z-10"
      />
    </div>
    <div class="space-y-4 text-center">
      <h3 class="text-xl font-mono text-zinc-300 tracking-tighter">
        Analyzing behavioral patterns...
      </h3>

      <!-- Barra de progreso simulada -->
      <div class="w-full h-1 bg-zinc-800 rounded-full overflow-hidden">
        <motion.div
          class="h-full bg-blue-600"
          :initial="{ width: '0%' }"
          :animate="{ width: '100%' }"
          :transition="{ duration: 2, repeat: Infinity }"
        />
      </div>

      <p
        class="text-[10px] uppercase tracking-[0.3em] text-zinc-500 animate-pulse"
      >
        Consulting global threat databases
      </p>
    </div>
  </motion.div>
</template>
