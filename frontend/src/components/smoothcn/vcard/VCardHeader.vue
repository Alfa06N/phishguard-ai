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
    data-slot="card-header"
    :class="
      cn(
        '@container/card-header grid auto-rows-min grid-rows-[auto_auto] items-start gap-1.5 px-6 has-data-[slot=card-action]:grid-cols-[1fr_auto] [.border-b]:pb-6',
        props.class,
      )
    "
  >
    <slot />
  </motion.div>
</template>
