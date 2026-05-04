<script setup>
import { VButton } from "./smoothcn/vbutton";
import { AlertCircle } from "lucide-vue-next";
import { useScanner } from "@/composables/useScanner";
import { motion } from "motion-v";
import { sVariants, sTransitions } from "@/lib/smoothcn";
import { storeToRefs } from "pinia";
const store = useScanner();
const { resetValues, performScan } = store;
const { error } = storeToRefs(store);
</script>

<template>
  <motion.div
    layout
    v-if="error"
    key="error"
    layout-id="results"
    v-bind="sVariants.fadeIn"
    :transition="sTransitions.spring.snappy"
    class="w-full border border-red-900/50 bg-red-950/10 rounded-2xl p-12 flex flex-col items-center justify-center min-h-[300px]"
  >
    <!-- Icono de Error con Pulso Crítico -->
    <div class="relative mb-8">
      <div
        class="absolute inset-0 rounded-full bg-red-500/20 animate-ping"
      ></div>
      <div
        class="p-4 bg-red-500/10 rounded-full border border-red-500/40 relative z-10"
      >
        <AlertCircle class="h-12 w-12 text-red-500" />
      </div>
    </div>

    <div class="space-y-4 text-center max-w-md">
      <h3 class="text-xl font-mono text-red-400 tracking-tighter uppercase">
        Analysis Interrupted
      </h3>

      <!-- Mensaje dinámico del error -->
      <p class="text-sm text-zinc-400 leading-relaxed">
        {{
          error.message ||
          "An unexpected error occurred while communicating with the intelligence nodes."
        }}
      </p>

      <!-- Botón de reintento para cerrar el flujo de UX -->
      <VButton
        variant="outline"
        @click="performScan"
        class="mt-6 px-6 py-2 rounded-lg text-zinc-300 text-xs font-bold uppercase tracking-widest"
      >
        Dismiss & Retry
      </VButton>

      <div
        class="pt-6 border-t border-red-900/20 text-xs font-mono text-red-400 uppercase tracking-widest"
      >
        Error: {{ error.status }}
      </div>
    </div>
  </motion.div>
</template>
