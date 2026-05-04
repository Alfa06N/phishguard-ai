<script setup lang="ts">
import { ref } from "vue";
import { useScanner } from "@/composables/useScanner";
import { Input } from "@/components/ui/input";
import { VButton } from "@/components/smoothcn/vbutton";
import {
  VCard,
  VCardAction,
  VCardContent,
  VCardDescription,
  VCardFooter,
  VCardHeader,
  VCardTitle,
} from "@/components/smoothcn/vcard";
import { Textarea } from "@/components/ui/textarea";

const inputContent = ref("");
const { isScanning, results, error, performScan } = useScanner();

const startAnalysis = () => {
  if (inputContent.value.trim()) {
    performScan(inputContent.value);
  }
};

const clearError = () => (error.value = null);
</script>

<template>
  <div
    class="flex flex-col min-h-screen w-full justify-center items-center px-2 py-4"
  >
    <VCard class="max-w-lg w-full">
      <VCardHeader>
        <VCardTitle>API testing</VCardTitle>
        <VCardDescription>Try here to test the api</VCardDescription>
      </VCardHeader>
      <VCardContent>
        <Textarea
          v-model="inputContent"
          placeholder="Paste URL here..."
          class="min-h-20 max-h-80"
        />
      </VCardContent>
      <CardFooter class="px-6 flex justify-end gap-2">
        <VButton v-if="error" variant="outline" @click="clearError"
          >Clear error</VButton
        >
        <VButton @click="startAnalysis" :disabled="isScanning">{{
          isScanning ? "Checking..." : "Run Scan"
        }}</VButton>
      </CardFooter>
    </VCard>
    <div v-if="results" style="margin-top: 2rem; color: green">
      <h3>Verdict: {{ results.verdict }}</h3>
      <pre>{{ JSON.stringify(results, null, 2) }}</pre>
    </div>

    <div v-if="error" style="margin-top: 2rem; color: red">
      <h3>Error {{ error.status }}</h3>
      <p>{{ error.message }}</p>
    </div>
  </div>

  <!-- <div style="padding: 2rem; font-family: sans-serif">
    <h1>Phishing Shield Debugger</h1>

    <input
      v-model="inputContent"
      placeholder="Paste URL here..."
      style="width: 100%; padding: 0.5rem; margin-bottom: 1rem"
    />

    <button @click="startAnalysis" :disabled="isScanning">
      {{ isScanning ? "Checking..." : "Run Scan" }}
    </button>

    <div v-if="results" style="margin-top: 2rem; color: green">
      <h3>Verdict: {{ results.verdict }}</h3>
      <pre>{{ JSON.stringify(results, null, 2) }}</pre>
    </div>

    <div v-if="error" style="margin-top: 2rem; color: red">
      <h3>Error {{ error.status }}</h3>
      <p>{{ error.message }}</p>
    </div>
  </div> -->
</template>
