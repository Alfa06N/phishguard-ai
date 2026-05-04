import { computed, ref } from "vue";
import api from "@/api";
import type { ScanResponse, ApiError, ScanStrategy } from "@/types";
import { getScanStrategy } from "./useScanStrategy";
import { defineStore } from "pinia";

export const useScanner = defineStore("scanner", () => {
  const isScanning = ref<boolean>(false);
  const results = ref<ScanResponse | null>(null);
  const error = ref<ApiError | null>(null);
  const inputValue = ref<string>("");
  const strategy = computed<null | ScanStrategy>(() =>
    results.value ? getScanStrategy(results.value) : null,
  );

  const performScan = async () => {
    const content = inputValue.value.trim();
    if (!content) return;
    isScanning.value = true;
    error.value = null;
    results.value = null;

    try {
      const data = await api.post<any, ScanResponse>("/scan", { content });
      results.value = data;
    } catch (err) {
      error.value = err as ApiError;
    } finally {
      isScanning.value = false;
    }
  };

  const setInputValue = (text: string) => {
    if (typeof text !== "string") return;
    inputValue.value = text;
  };

  const resetValues = () => {
    isScanning.value = false;
    results.value = null;
    error.value = null;
    inputValue.value = "";
  };

  return {
    isScanning,
    inputValue,
    results,
    error,
    strategy,
    performScan,
    resetValues,
    setInputValue,
  };
});
