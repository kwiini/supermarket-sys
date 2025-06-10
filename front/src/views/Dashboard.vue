<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useStore } from '../stores/store';

const store = useStore();
const statistics = ref([
  { label: '总会员数', value: 0 },
  { label: '总产品数', value: 0 },
  { label: '总销售额', value: 0 },
  { label: '总采购额', value: 0 },
]);

onMounted(() => {
  // store.fetchMembers();
  // store.fetchProducts();
  // store.fetchSales();
  // store.fetchPurchases();
  updateStatistics();
});

const updateStatistics = () => {
  statistics.value[0].value = store.members.length;
  statistics.value[1].value = store.products.length;
  statistics.value[2].value = store.sales.reduce((total, sale) => total + sale.total_amount, 0);
  statistics.value[3].value = store.purchases.reduce((total, purchase) => total + purchase.total_price, 0);
};
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
      <h2 class="m-0 font-bold tracking-wide">欢迎使用超超批发系统</h2>
    </el-header>


    <el-main>
      <el-row :gutter="20">
        <el-col :span="6" v-for="stat in statistics" :key="stat.label">
          <el-card class="bg-[#f4f4f4] p-4 text-center border rounded-lg">
            <h3>{{ stat.label }}</h3>
            <p>{{ stat.value }}</p>
          </el-card>
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>
