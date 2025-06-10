<script setup lang="ts">
import { onMounted } from 'vue';
import { useStore } from '../stores/store';

const store = useStore();

onMounted(() => {
  // store.fetchPurchases();
});

const purchases = store.purchases;
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
      <h2 class="m-0 font-bold tracking-wide">采购管理</h2>
    </el-header>
    
    <el-main class="mt-5 p-4 bg-gray-50 rounded-lg shadow-inner">
      <el-table :data="purchases" style="width: 100%">
        <el-table-column prop="purchase_id" label="采购ID" />
        <el-table-column prop="purchase_date" label="采购日期" />
        <el-table-column prop="supplier_id" label="供应商ID" />
        <el-table-column prop="total_price" label="总价" />
        <el-table-column prop="employee_id" label="员工ID" />
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