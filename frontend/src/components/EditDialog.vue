<template>
    <div v-if="isVisible" class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50">
        <div class="bg-white p-6 rounded-lg shadow-lg w-1/3">
            <h2 class="text-xl font-bold mb-4">Edit Information</h2>
            <form @submit.prevent="handleSubmit">
                <div class="mb-4">
                    <label for="name" class="block text-gray-700">Name</label>
                    <input v-model="form.name" id="name" type="text"
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm" />
                </div>
                <div class="mb-4">
                    <label for="gender" class="block text-gray-700">Gender</label>
                    <select v-model="form.gender" id="gender"
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm">
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        <option value="other">Other</option>
                    </select>
                </div>
                <div class="flex justify-end">
                    <button type="button" @click="handleCancel"
                        class="bg-gray-500 text-white px-4 py-2 rounded-md mr-2">Cancel</button>
                    <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-md">Confirm</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';

const props = defineProps<{
    isVisible: boolean;
    defaultValues?: { name: string, gender: string };
}>();

const emit = defineEmits(['update:isVisible', 'submit']);

const form = ref({ ...props.defaultValues });

watch(() => props.defaultValues, (newValues) => {
    form.value = { ...newValues };
});

const handleCancel = () => {
    emit('update:isVisible', false);
    form.value = {}
};

const handleSubmit = () => {
    emit('submit', form.value);
    emit('update:isVisible', false);
    form.value = {}
};
</script>

<style scoped>
/* Add any additional styles if needed */
</style>