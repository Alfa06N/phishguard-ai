<script setup lang="ts">
import type { HTMLAttributes } from "vue";
import { cn } from "@/lib/utils";
import { motion, LayoutGroup } from "motion-v";
import { sTransitions } from "@/lib/smoothcn/transitions";

const props = defineProps<{
  class?: HTMLAttributes["class"];
  layoutId?: string;
  disableLayoutGroup?: boolean;
}>();
</script>

<template>
  <LayoutGroup v-if="!disableLayoutGroup" :layout-id="layoutId">
    <motion.div
      layout
      :transition="sTransitions.spring.snappy"
      data-slot="card"
      :class="
        cn(
          'bg-card text-card-foreground flex flex-col gap-6 rounded-xl border py-6 shadow-sm',
          props.class,
        )
      "
    >
      <slot />
    </motion.div>
  </LayoutGroup>

  <motion.div
    v-else
    layout
    :layout-id="layoutId"
    :transition="sTransitions.spring.snappy"
    data-slot="card"
    :class="
      cn(
        'bg-card text-card-foreground flex flex-col gap-6 rounded-xl border py-6 shadow-sm',
        props.class,
      )
    "
  >
    <slot />
  </motion.div>
</template>
