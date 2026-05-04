<script setup lang="ts">
import type { PrimitiveProps } from "reka-ui";
import type { HTMLAttributes } from "vue";
import type { ButtonVariants } from ".";
import { Primitive } from "reka-ui";
import { cn } from "@/lib/utils";
import { buttonVariants } from ".";
import { Motion } from "motion-v";
import { sGestures, sTransitions } from "@/lib/smoothcn";

interface Props extends PrimitiveProps {
  variant?: ButtonVariants["variant"];
  size?: ButtonVariants["size"];
  class?: HTMLAttributes["class"];
}

const props = withDefaults(defineProps<Props>(), {
  as: "button",
});
</script>

<template>
  <Motion
    as-child
    :transition="variant !== 'link' ? sTransitions.spring.solid : {}"
    :while-press="variant !== 'link' ? sGestures.press.whilePress : {}"
  >
    <Primitive
      data-slot="button"
      :data-variant="variant"
      :data-size="size"
      :as="as"
      :as-child="asChild"
      :class="cn(buttonVariants({ variant, size }), props.class)"
    >
      <slot />
    </Primitive>
  </Motion>
</template>
