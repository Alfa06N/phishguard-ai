<script setup lang="ts">
import { ArrowUpRight } from "lucide-vue-next";
import { useScanner } from "@/composables/useScanner";

defineProps({
  item: {
    type: Object,
    required: true,
  },
});

defineEmits(["select"]);
const { setInputValue, scrollToInput } = useScanner();

const handleClick = (text: string) => {
  setInputValue(text);
  scrollToInput();
};
</script>

<template>
  <button
    @click="handleClick(item.text)"
    class="flex flex-col gap-2 p-4 w-72 text-left rounded-xl border border-zinc-800 bg-zinc-900/40 hover:border-zinc-500 hover:bg-zinc-800/60 transition-all duration-300 group/card cursor-pointer"
  >
    <div class="flex justify-between items-center">
      <span
        :class="[
          'text-[10px] font-bold uppercase tracking-widest px-2 py-0.5 rounded border border-current bg-opacity-10',
          item.color,
        ]"
      >
        {{ item.label }}
      </span>
      <!-- Un pequeño icono que aparece al hacer hover para indicar que es clickable -->
      <ArrowUpRight
        class="w-3 h-3 text-zinc-600 group-hover/card:text-zinc-300 transition-colors"
      />
    </div>

    <p
      class="text-sm text-zinc-400 line-clamp-2 italic group-hover/card:text-zinc-200 transition-colors"
    >
      "{{ item.text }}"
    </p>
  </button>
</template>
