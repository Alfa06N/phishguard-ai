<script setup lang="ts">
import type { HTMLAttributes } from "vue";
import { cn } from "@/lib/utils";
import { motion } from "motion-v";
import { sTransitions } from "@/lib/smoothcn/transitions";

const props = defineProps<{
  class?: HTMLAttributes["class"];
}>();
</script>

<template>
  <motion.div
    layout
    :transition="sTransitions.spring.snappy"
    data-slot="card-footer"
    :class="cn('flex items-center px-6 [.border-t]:pt-6', props.class)"
  >
    <slot />
  </motion.div>
</template>
