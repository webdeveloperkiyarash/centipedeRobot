<template>
    <div :dir="useLanguageStore().language == 'fa' ? 'rtl' : 'ltr'"
        class="d-flex flex-column align-center gap-2 width-window py-2 px-4 height-full position-relative bg-neutral-800 text-white">
        <h1>{{ $t('emergency.title') }}</h1>
        <RouterLink to="/"
            class="button-style-2 position-absolute top left border-none outline-none d-flex align-flex-start radius-2 bg-neutral-700">
            <Icon icon="solar:arrow-left-linear" class="text-white" width="35" />
        </RouterLink>
        <img src="/images/error.png" class="width-full height-full max-width-300 max-height-300" alt="" />
        <pre class="font-size-4">{{ $t(`emergency.description`) }}</pre>
        <div class="d-flex align-center gap-4">
            <button @click="enabled = true" :class="enabled ? 'bg-red-500' : 'bg-neutral-700'"
                class="button-style-2 text-white text-center px-6 font-size-5 border-none outline-none radius-10 py-2 font-500">
                {{ $t('emergency.enabled') }}
            </button>
            <button @click="enabled = false"
                class="button-style-2 text-white text-center px-6 font-size-5 bg-neutral-700 border-none outline-none radius-10 py-2 font-500">
                {{ $t('emergency.disabled') }}
            </button>
        </div>
    </div>
</template>


<script setup lang="ts">
import { useLanguageStore } from '@/stores/useLanguage';
import { Icon } from '@iconify/vue';
import { ref } from 'vue';
const enabled = ref(false);

</script>

<style lang="scss" scoped></style>