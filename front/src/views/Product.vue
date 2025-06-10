<script setup lang="ts">
import { onMounted } from 'vue';
import { useStore } from '../stores/store';

const store = useStore();

onMounted(() => {
  // store.fetchProducts();
});

const products = store.products;
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
      <h2 class="m-0 font-bold tracking-wide">产品管理</h2>
    </el-header>

    <el-main class="mt-5 p-4 bg-gray-50 rounded-lg shadow-inner">
      <el-table :data="products" style="width: 100%">
        <el-table-column prop="product_id" label="产品ID" />
        <el-table-column prop="name" label="产品名称" />
        <el-table-column prop="category" label="类别" />
        <el-table-column prop="purchase_price" label="采购价" />
        <el-table-column prop="selling_price" label="销售价" />
        <el-table-column prop="description" label="描述" />
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