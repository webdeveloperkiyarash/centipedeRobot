<template>
    <div
        class="d-flex flex-column align-center gap-2 width-window py-2 px-4 height-full position-relative bg-neutral-800 text-white">
        <h1>emergency mode</h1>
        <!-- Back Button -->
        <RouterLink to="/"
            class="button-style-2 position-absolute top left border-none outline-none d-flex align-flex-start radius-2 bg-neutral-700">
            <Icon icon="solar:arrow-left-linear" class="text-white" width="35" />
        </RouterLink>
        <img src="/images/error.png" class="width-full height-full max-width-300 max-height-300" alt="" />
        <p class="font-size-4">
            ⚠️ <strong>Emergency Mode</strong>: In critical situations, the robot may enter an emergency state.
            <br>
            🔋 Low Battery – when the power level drops dangerously, the system prioritizes safe shutdown or return.
            <br>
            🧭 Lost Navigation – if the robot loses its path or orientation, emergency protocols are triggered to
            prevent further risk.
            <br>
            ↩️ Return Back – the robot can decide to retrace its steps to a safe location.
            <br>
            🤖 In all cases, the AI evaluates the context and decides which option is the most effective response.
        </p>
        <div class="d-flex align-center gap-4">
            <button @click="enabled = true" :class="enabled ? 'bg-red-500' : 'bg-neutral-700'"
                class="button-style-2 text-white text-center px-6 font-size-5 border-none outline-none radius-10 py-2 font-500">
                enabled
            </button>
            <button @click="enabled = false"
                class="button-style-2 text-white text-center px-6 font-size-5 bg-neutral-700 border-none outline-none radius-10 py-2 font-500">
                disabled
            </button>
        </div>
    </div>
</template>

<script setup lang="ts">
import { Icon } from '@iconify/vue';
import { ref } from 'vue';
const enabled = ref(false);

</script>

<style lang="scss" scoped></style>