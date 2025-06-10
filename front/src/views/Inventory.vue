<script setup lang="ts">
import { onMounted } from 'vue';
import { useStore } from '../stores/store';

const store = useStore();

onMounted(() => {
  // store.fetchInventory();
});

const inventory = store.inventory;
</script>

<template>
  <el-container>
    <el-header
      class="text-xl text-white flex items-center justify-center shadow-lg rounded-lg"
      style="
        height: 64px;
        background: radial-gradient(circle at top left, #34d399, #10b981, #059669);
      "
    >
      <h2 class="m-0 font-bold tracking-wide">库存管理</h2>
    </el-header>

    <el-main class="mt-5 p-4 bg-gray-50 rounded-lg shadow-inner">
      <el-table :data="inventory" style="width: 100%" class="bg-white rounded-md shadow">
        <el-table-column prop="inventory_id" label="库存ID" />
        <el-table-column prop="product_id" label="产品ID" />
        <el-table-column prop="batch_number" label="批次号" />
        <el-table-column prop="production_date" label="生产日期" />
        <el-table-column prop="expiry_date" label="过期日期" />
        <el-table-column prop="quantity" label="数量" />
        <el-table-column prop="location" label="存储位置" />
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