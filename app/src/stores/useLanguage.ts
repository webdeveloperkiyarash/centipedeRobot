import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const useLanguageStore = defineStore("useLanguageStore", () => {
    const language = ref<"fa" | "us">(
        (localStorage.getItem("app-language") as "fa" | "us") || "us"
    );

    const toggleLanguage = () => {
        language.value = language.value === "us" ? "fa" : "us";
        saveToLocalStorage();
    };

    const languageIcon = computed(() => {
        return language.value === "us"
            ? "circle-flags:fa" // آیکون انگلیسی
            : "circle-flags:us";      // آیکون فارسی
    });

    const saveToLocalStorage = () => {
        localStorage.setItem("app-language", language.value);
    };

    return {
        language,
        toggleLanguage,
        languageIcon,
        saveToLocalStorage,
    };
});
