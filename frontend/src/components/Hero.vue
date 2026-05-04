<script setup lang="ts">
import { ShieldCheck } from "lucide-vue-next";
import { Textarea } from "@/components/ui/textarea";
import { computed } from "vue";
import { useScanner } from "@/composables/useScanner";
import { VButton } from "@/components/smoothcn/vbutton";
import { storeToRefs } from "pinia";
import { motion } from "motion-v";
import { sTransitions } from "@/lib/smoothcn";

const store = useScanner();
const { performScan } = store;
const { isScanning, inputValue, inputRef } = storeToRefs(store);
const MAX_LENGTH = 3000;

const charCount = computed(() => inputValue.value.length);
const isOverLimit = computed(() => charCount.value > MAX_LENGTH);
</script>

<template>
  <motion.section
    layout
    :transition="sTransitions.spring.snappy"
    class="relative flex min-h-screen flex-col items-center justify-start md:justify-center px-4 pt-20 pb-12 text-center"
  >
    <div
      class="mb-6 inline-flex items-center rounded-full border border-zinc-800 bg-zinc-900/50 px-3 py-1 text-xs font-medium text-zinc-400"
    >
      <ShieldCheck class="mr-2 h-4 w-4" /> AI-Powered Phishing Protection
    </div>

    <h1
      class="max-w-2-4xl bg-linear-to-b from-zinc-50 to-zinc-400 bg-clip-text text-5xl font-bold tracking-tight text-transparent sm:text-7xl"
    >
      PhishGuard AI
    </h1>

    <p class="mt-6 max-w-2xl text-lg leading-8 text-zinc-400">
      Analyze suspicious emails, URLs and attachments for phishing risks in
      real-time. Combining heuristic AI intelligence with global threat
      databases.
    </p>

    <div class="mt-10 w-full max-w-xl">
      <div
        ref="inputRef"
        class="group relative rounded-xl border border-zinc-800 bg-zinc-900/40 p-2 transition-all duration-300 focus-within:border-zinc-400 focus-within:shadow-[0_0_30px_rgba(255,255,255,0.05),0_0_10px_rgba(255,255,255,0.05)]"
      >
        <Textarea
          v-model="inputValue"
          max-length="3000"
          placeholder="Paste email content or URL here..."
          class="w-full h-20 resize-none border-none bg-transparent p-4 outline-none focus:ring-0"
        />
        <div class="flex justify-between items-center mt-2">
          <span
            :class="[
              'text-xs pl-2',
              isOverLimit ? 'text-red-500' : 'text-zinc-500',
            ]"
            >{{ charCount }}/{{ MAX_LENGTH }}</span
          >
          <VButton @click="performScan" :disabled="isScanning">
            {{ isScanning ? "Analyzing..." : "Scan Content" }}
          </VButton>
        </div>
      </div>
    </div>
  </motion.section>
</template>
