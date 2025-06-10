<script setup lang="ts">
import { onMounted } from 'vue';
import { useStore } from '../stores/store';

const store = useStore();

onMounted(() => {
  // store.fetchSales();
});

const sales = store.sales;
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
      <h2 class="m-0 font-bold tracking-wide">销售管理</h2>
    </el-header>
    
    <el-main class="mt-5 p-4 bg-gray-50 rounded-lg shadow-inner">
      <el-table :data="sales" style="width: 100%">
        <el-table-column prop="sale_id" label="销售ID" />
        <el-table-column prop="sale_date" label="销售日期" />
        <el-table-column prop="member_id" label="会员ID" />
        <el-table-column prop="total_amount" label="总金额" />
        <el-table-column prop="discount_amount" label="优惠金额" />
        <el-table-column prop="payment_method" label="支付方式" />
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