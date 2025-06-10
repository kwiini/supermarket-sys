<script setup lang="ts">
import { useStore } from '../stores/store';
import { onMounted } from 'vue';

const store = useStore();

onMounted(() => {
  store.fetchMembers();
});

const members = store.members;
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
      <h2 class="m-0 font-bold tracking-wide">会员管理</h2>
    </el-header>

    <el-main class="mt-5 p-4 bg-gray-50 rounded-lg shadow-inner">
      <el-table :data="members" style="width: 100%;">
        <el-table-column prop="member_id" label="会员ID" width="100" />
        <el-table-column prop="name" label="姓名" width="120" />
        <el-table-column prop="phone" label="电话" width="150" />
        <el-table-column prop="email" label="邮箱" width="200" />
        <el-table-column prop="register_date" label="注册日期" width="150" />
        <el-table-column prop="expiry_date" label="到期日期" width="150" />
      </el-table>
    </el-main>
  </el-container>
</template>