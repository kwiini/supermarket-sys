<script setup lang="ts">
import { onMounted, ref, computed } from 'vue';
import { useMemberStore, useEmployeeStore, useProductStore, useSaleStore } from '../stores/index';

const currentTime = ref('');
const greeting = computed(() => {
  const hour = new Date().getHours();
  if (hour < 6 && hour >= 1) {
    return '凌晨好';
  }
  if (hour < 11 && hour >= 6) {
    return '早上好';
  }
  if (hour < 15 && hour >= 11) {
    return '中午好';
  }
  if (hour < 18 && hour >= 15) {
    return '下午好';
  }
  return '晚上好';
});

const updateTime = () => {
  const now = new Date();
  currentTime.value = now.toLocaleString();
};
setInterval(updateTime, 1000);
updateTime();

const statistics = ref([
  { label: '总会员数', value: 0 },
  { label: '总员工数', value: 0 },
  { label: '总产品数', value: 0 },
  { label: '总销售额', value: 0 },
]);

const recentMembers = computed(() => {
  return [...useMemberStore().members].slice(-5).reverse();
});

const announcements = ref([
  '系统正在维护中，数据请定期备份。',
  '本月促销活动已开始，请关注销售数据。',
]);

onMounted(async () => {
  await Promise.all([
    useMemberStore().fetchMembers(),
    useEmployeeStore().fetchEmployee(),
    useProductStore().fetchProducts(),
    useSaleStore().fetchSales()
  ]);
  updateStatistics();
});

const updateStatistics = () => {
  statistics.value[0].value = useMemberStore().members.length;
  statistics.value[1].value = useEmployeeStore().employee.length;
  statistics.value[2].value = useProductStore().products.length;
  statistics.value[3].value = useSaleStore().sales.reduce((total, sale) => total + sale.total_amount, 0);
};
</script>

<template>
  <el-container>
    <!-- 顶部欢迎语 -->
    <el-header
      class="text-xl text-white flex items-center justify-between shadow-lg px-6 rounded-lg"
      style="height: 64px; background: radial-gradient(circle at top left, #34d399, #10b981, #059669);"
    >
      <h3 class="font-bold tracking-wide">{{ greeting }}，欢迎使用超市后台管理系统</h3>
      <div class="text-sm">{{ currentTime }}</div>
    </el-header>

    <el-main class="space-y-6">
      <!-- 数据统计 -->
      <el-row :gutter="20">
        <el-col :span="6" v-for="stat in statistics" :key="stat.label">
          <el-card class="p-4 text-center border rounded-lg">
            <h3>{{ stat.label }}</h3>
            <p class="text-2xl font-semibold">{{ stat.value }}</p>
          </el-card>
        </el-col>
      </el-row>

      <!-- 最近活动 -->
      <el-card class="rounded-lg">
        <template #header>
          <span class="font-semibold text-lg">最近新增会员</span>
        </template>
        <el-timeline>
          <el-timeline-item
            v-for="member in recentMembers"
            :key="member.member_id"
            :timestamp="member.register_date"
            color="#10b981"
          >
            {{ member.name }} - {{ member.register_date }}
          </el-timeline-item>
        </el-timeline>
      </el-card>

      <!-- 系统公告 -->
      <el-card class="rounded-lg">
        <template #header>
          <span class="font-semibold text-lg">系统公告</span>
        </template>
        <ul class="list-disc pl-6 space-y-1">
          <li v-for="(item, index) in announcements" :key="index">{{ item }}</li>
        </ul>
      </el-card>
    </el-main>
  </el-container>
</template>
