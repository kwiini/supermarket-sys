<script setup lang="ts">
import { onMounted, computed, ref } from 'vue';
import { useSupplierStore } from '../stores/index';
import AddDialog from '../components/AddDialog.vue';
import type { FieldSchema } from '../components/AddDialog.vue';

const store = useSupplierStore();
const dialogRef = ref();

onMounted(() => {
  store.fetchSuppliers();
});

const openAddDialog = () => {
  dialogRef.value.open();
};

const suppliersSchema: FieldSchema[] = [
  { label: '供应商名称', prop: 'name', type: 'input' },
  { label: '联系人', prop: 'contact_person', type: 'input' },
  { label: '联系电话', prop: 'phone', type: 'input', attrs: { placeholder: '请输入手机号' } },
  { label: '电子邮箱', prop: 'email', type: 'input', attrs: { placeholder: 'example@company.com' } },
  { label: '地址', prop: 'address', type: 'input' },
  { label: '供应品类', prop: 'supply_category', type: 'input' },
  { label: '供应商编号', prop: 'supplier_id', type: 'input' }
];


const addSuppliers = async (data: any) => {
  await store.addSuppliers(data);
  await store.fetchSuppliers();
};

const suppliers = computed(() => store.suppliers);;
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
      <el-button type="success" @click="openAddDialog">新增供应商</el-button>

      <el-table :data="suppliers" style="width: 100%; margin-top: 16px;" size="large">
        <el-table-column prop="name" label="供应商名称" />
        <el-table-column prop="contact_person" label="联系人" />
        <el-table-column prop="phone" label="联系电话" />
        <el-table-column prop="email" label="电子邮箱" />
        <el-table-column prop="address" label="地址" />
        <el-table-column prop="supply_category" label="供应品类" />
        <el-table-column prop="supplier_id" label="供应商编号" />

        <el-table-column label="操作" width="100">
          <template #default="{ row }">
            <el-button type="danger" size="small" @click="store.deleteSuppliers(row.supplier_id)">删除</el-button>
          </template>
        </el-table-column>
        
      </el-table>
    </el-main>
  </el-container>

  <add-dialog
    ref="dialogRef"
    title="新增员工"
    :formSchema="suppliersSchema"
    :submitHandler="addSuppliers"
  />

</template>