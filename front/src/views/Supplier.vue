<script setup lang="ts">
import { onMounted } from 'vue';
import { useStore } from '../stores/store';

const store = useStore();

onMounted(() => {
  // store.fetchSuppliers();
});

const suppliers = store.suppliers;
</script>

<template>
  <el-container>
    <el-header
      class="text-xl text-white flex items-center justify-center shadow-lg"
      style="
        height: 64px;
        background: radial-gradient(circle at top left, #34d399, #10b981, #059669);
      "
    >
      <h2 class="m-0 font-bold tracking-wide">供应商管理</h2>
    </el-header>

    <el-main class="mt-5 p-4 bg-gray-50 rounded-lg shadow-inner">
      <el-table :data="suppliers" style="width: 100%">
        <el-table-column prop="supplier_id" label="供应商ID" />
        <el-table-column prop="name" label="供应商名称" />
        <el-table-column prop="contact_person" label="联系人" />
        <el-table-column prop="phone" label="电话" />
        <el-table-column prop="email" label="邮箱" />
        <el-table-column prop="supply_category" label="供货类别" />
      </el-table>
    </el-main>
  </el-container>
</template>

<style scoped>
.el-header {
  background-color: #409EFF;
  color: #fff;
  padding: 20px;
  text-align: center;
}
</style>