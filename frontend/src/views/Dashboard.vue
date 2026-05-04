<script setup lang="ts">
import { StarsBackground } from "@/components/ui/bg-stars";
import Hero from "@/components/Hero.vue";
import ScanResults from "@/components/ScanResults.vue";
import Footer from "@/components/Footer.vue";
import InfiniteMarquee from "@/components/InfiniteMarquee.vue";
import { LayoutGroup, motion, AnimatePresence } from "motion-v";
import LoadingState from "@/components/LoadingState.vue";
import ErrorState from "@/components/ErrorState.vue";
import { sTransitions } from "@/lib/smoothcn";
</script>

<template>
  <div class="relative min-h-screen w-full flex flex-col">
    <StarsBackground
      :factor="0.05"
      :speed="50"
      class="absolute inset-0 z-0 opacity-40"
    />
    <LayoutGroup>
      <motion.main class="relative z-10 flex flex-1 flex-col items-center">
        <Hero />
        <motion.div
          layout
          :transition="sTransitions.spring.snappy"
          class="min-w-sm relative overflow-hidden px-4"
        >
          <AnimatePresence mode="popLayout">
            <LoadingState />
            <ScanResults />
            <ErrorState />
          </AnimatePresence>
        </motion.div>

        <InfiniteMarquee />
        <Footer />
      </motion.main>
    </LayoutGroup>
  </div>
</template>
