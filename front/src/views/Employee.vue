<script setup lang="ts">
import { useEmployeeStore } from '../stores/index';
import { onMounted, computed, ref } from 'vue';
import AddDialog from '../components/AddDialog.vue';
import type { FieldSchema } from '../components/AddDialog.vue';

const store = useEmployeeStore();
const dialogRef = ref();

onMounted(() => {
  store.fetchEmployee();
});

const openAddDialog = () => {
  dialogRef.value.open();
};

const employeeSchema: FieldSchema[] = [
  { label: '姓名', prop: 'name', type: 'input' },
  { label: '职位', prop: 'position', type: 'input' },
  { label: '电话', prop: 'phone', type: 'input', attrs: { placeholder: '请输入手机号' } },
  { label: '邮箱', prop: 'email', type: 'input', attrs: { placeholder: 'example@company.com' } },
  { label: '入职日期', prop: 'hire_date', type: 'date', attrs: { placeholder: '选择日期'} },
  { label: '薪水', prop: 'salary', type: 'input', attrs: { type: 'number', min: 0 } },
  { label: '上级经理编号', prop: 'manager_id', type: 'input' },
  { label: '员工编号', prop: 'employee_id', type: 'input' },
];


const addEmployee = async (data: any) => {
  await store.addEmployee(data);
  await store.fetchEmployee();
};

const employee = computed(() => store.employee);
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
      <h2 class="m-0 font-bold tracking-wide">员工管理</h2>
    </el-header>

    <el-main class="mt-5 p-4 bg-gray-50 rounded-lg shadow-inner">
      <el-button type="success" @click="openAddDialog">新增员工</el-button>

      <el-table :data="employee" style="width: 100%; margin-top: 16px;" size="large">
        <el-table-column prop="name" label="姓名" />
        <el-table-column prop="position" label="职位" />
        <el-table-column prop="phone" label="电话" />
        <el-table-column prop="email" label="电子邮箱"/>
        <el-table-column prop="hire_date" label="入职日期" />
        <el-table-column prop="salary" label="薪水" />
        <el-table-column prop="manager_id" label="上级经理编号" />
        <el-table-column prop="employee_id" label="员工编号"  />

        <el-table-column label="操作" width="100">
          <template #default="{ row }">
            <el-button type="danger" size="small" @click="store.deleteEmployee(row.employee_id)">删除</el-button>
          </template>
        </el-table-column>

      </el-table>
    </el-main>
  </el-container>

  <add-dialog
    ref="dialogRef"
    title="新增员工"
    :formSchema="employeeSchema"
    :submitHandler="addEmployee"
  />
</template>