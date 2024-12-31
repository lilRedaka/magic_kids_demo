<template>
  <div class="p-6">
    <!-- Add User Button -->
    <button @click="() => handleOpenEditDialog()" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
      Add User
    </button>

    <!-- User Table -->
    <div class="mt-4 overflow-x-auto">
      <table class="table-auto w-full border-collapse border border-gray-200">
        <thead>
          <tr class="bg-gray-100">
            <th class="border border-gray-300 px-4 py-2 text-left">ID</th>
            <th class="border border-gray-300 px-4 py-2 text-left">Name</th>
            <th class="border border-gray-300 px-4 py-2 text-left">Gender</th>
            <th class="border border-gray-300 px-4 py-2 text-left">Edit</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id" class="hover:bg-gray-50">
            <td class="border border-gray-300 px-4 py-2">{{ user.id }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ user.name }}</td>
            <td class="border border-gray-300 px-4 py-2">{{ user.gender }}</td>
            <td class="border border-gray-300 px-4 py-2">
              <button @click="() => handleOpenEditDialog(user)"
                class="bg-green-500 text-white px-3 py-1 rounded hover:bg-green-600">
                Edit
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Pagination -->
    <div class="flex justify-center mt-4 space-x-2">
      <button class="px-3 py-1 border rounded hover:bg-gray-100" @click="prevPage" :disabled="currentPage === 1">
        < </button>
          <button v-for="page in Math.ceil(totalPages/5)" :key="page" class="px-3 py-1 border rounded hover:bg-gray-100"
            :class="{ 'bg-blue-500 text-white': currentPage === page }" @click="goToPage(page)">
            {{ page }}
          </button>
          <button class="px-3 py-1 border rounded hover:bg-gray-100" @click="nextPage"
            :disabled="currentPage === totalPages">
            >
          </button>
    </div>
  </div>
  <EditDialog :is-visible="isEditDialogVisible" v-on:submit="handleEditDialogSubmit"
    :default-values="editDialogDefaultValues" v-on:update:is-visible="handleCloseEditDialog" />
</template>

<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import EditDialog from '@/components/EditDialog.vue'
import { addUser, editUser, getUsers } from '@/api'
// edit
const isEditDialogVisible = ref(false);
const editDialogDefaultValues = ref<{ name: string, gender: string } | undefined>(undefined);

const handleOpenEditDialog = (defaultValues?: { name: string, gender: string }) => {
  if (defaultValues) {
    editDialogDefaultValues.value = defaultValues;
  } else {
    editDialogDefaultValues.value = undefined
  }
  isEditDialogVisible.value = true;
};

const handleCloseEditDialog = () => {
  isEditDialogVisible.value = false;
  editDialogDefaultValues.value = undefined
};

const handleEditDialogSubmit = async (values: any) => {
  if (values.id) {
    const res = await editUser(values.id, values.name, values.gender)
  } else {
    const res = await addUser(values.name, values.gender)
  }

  getUsersData()
  editDialogDefaultValues.value = undefined
}


// user list
interface User {
  id: number;
  name: string;
  gender: string;
}

const users = ref<User[]>([]);

const currentPage = ref<number>(1);
const totalPages = ref<number>(0); // Adjust this based on your data

const getUsersData = async () => {
  const response = await getUsers(currentPage.value);
  users.value = response.data
  totalPages.value = response.total
  currentPage.value = response.page
};

onMounted(() => {
  getUsersData();
});

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
    getUsersData()
  };
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
    getUsersData()
  };
};

const goToPage = (page: number) => {
  currentPage.value = page;
  getUsersData()
};
</script>

<style scoped></style>