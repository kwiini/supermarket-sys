<script setup lang="ts">
import Navbar from './components/Navbar.vue';
import Sidebar from './components/Sidebar.vue';
</script>

<template>
  <div id="app" class="flex flex-col h-screen">
    <Navbar />
    <div class="flex flex-row flex-1 mt-4 overflow-hidden">
      <Sidebar />
      <div class="flex-1 overflow-auto px-5 py-2">
        <router-view />
      </div>
    </div>
  </div>
</template>

<style scoped>
#app {
  min-height: 100vh;
  background: linear-gradient(to right, #a7f3d0 , #d1fae5, #f0fdf4);
}
</style>



