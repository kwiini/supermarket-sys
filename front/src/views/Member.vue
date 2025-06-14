<script setup lang="ts">
import { useMemberStore } from '../stores/index';
import { onMounted, computed, ref } from 'vue';
import AddDialog from '../components/AddDialog.vue';
import type { FieldSchema } from '../components/AddDialog.vue';

const store = useMemberStore();
const dialogRef = ref();

onMounted(() => {
  store.fetchMembers();
});

const openAddDialog = () => {
  dialogRef.value.open();
};

const membersSchema: FieldSchema[] = [
  { label: '姓名', prop: 'name', type: 'input' },
  { label: '电话', prop: 'phone', type: 'input', attrs: { placeholder: '请输入手机号' } },
  { label: '邮箱', prop: 'email', type: 'input', attrs: { placeholder: 'example@company.com' } },
  { label: '地址', prop: 'address', type: 'input' },
  { label: '注册日期', prop: 'register_date', type: 'date', attrs: { placeholder: '选择注册日期' } },
  { 
    label: '会员类型', 
    prop: 'member_type', 
    type: 'select', 
    attrs: { options: [
        { label: '普通', value: '普通' },
        { label: '黄金', value: '黄金' }
      ] } 
  },
  { label: '到期日期', prop: 'expiry_date', type: 'date', attrs: { placeholder: '选择到期日期' } },
  { label: '会员编号', prop: 'member_id', type: 'input' },
];


const addMembers = async (data: any) => {
  await store.addMembers(data);
  await store.fetchMembers();
};

const members = computed(() => store.members);
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
      <el-button type="success" @click="openAddDialog">新增会员</el-button>
      
      <el-table :data="members" style="width: 100%; margin-top: 16px;" size="large">
        <el-table-column prop="name" label="姓名" />
        <el-table-column prop="phone" label="电话" />
        <el-table-column prop="email" label="电子邮箱"/>
        <el-table-column prop="address" label="地址"/>
        <el-table-column prop="register_date" label="注册日期" />
        <el-table-column prop="member_type" label="会员类型" />
        <el-table-column prop="expiry_date" label="到期日期" />
        <el-table-column prop="member_id" label="会员编号"  />

        <el-table-column label="操作" width="100">
          <template #default="{ row }">
            <el-button type="danger" size="small" @click="store.deleteMembers(row.member_id)">删除</el-button>
          </template>
        </el-table-column>

      </el-table>
    </el-main>
  </el-container>

  <add-dialog
    ref="dialogRef"
    title="新增会员"
    :formSchema="membersSchema"
    :submitHandler="addMembers"
  />
</template>