<script setup lang="ts">
import Navbar from './components/Navbar.vue';
import Sidebar from './components/Sidebar.vue';
</script>

<template>
  <div id="app" class="flex flex-col">
    <Navbar />
    <div class="flex flex-row mt-4 px-2">
      <Sidebar />
      <div class="flex-1 px-5 py-2">
        <router-view />
      </div>
    </div>
  </div>
</template>

<style scoped>
#app {
  height: 98vh;
  background: linear-gradient(to right, #a7f3d0 , #d1fae5, #f0fdf4);
}
</style>

