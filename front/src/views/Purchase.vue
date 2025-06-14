<script setup lang="ts">
import { onMounted, computed, ref } from 'vue';
import { usePurchaseStore, useEmployeeStore } from '../stores/index';
import AddDialog from '../components/AddDialog.vue';
import type { FieldSchema } from '../components/AddDialog.vue';

const store = usePurchaseStore();
const emplyeeStore = useEmployeeStore();
const dialogRef = ref();

onMounted(() => {
  store.fetchPurchases();
  emplyeeStore.fetchEmployee();
});

const openAddDialog = () => {
  dialogRef.value.open();
};

const emplyeeOptions = computed(() =>
  emplyeeStore.employee.map(e => ({
    label: `${e.employee_id} - ${e.name}`,
    value: e.employee_id,
  }))
);

const purchasesSchema: FieldSchema[] = [
  { label: '供应商编号', prop: 'supplier_id', type: 'input' },
  { label: '商品编号', prop: 'product_id', type: 'input' },
  { label: '采购日期', prop: 'purchase_date', type: 'date', attrs: { placeholder: '选择采购日期' } },
  { label: '数量', prop: 'quantity', type: 'number', attrs: { min: 1 } },
  { label: '单价', prop: 'unit_price', type: 'number', attrs: { min: 0 } },
  { label: '总价', prop: 'total_price', type: 'number', attrs: { min: 0 } },
  {
    label: '经办员工编号',
    prop: 'employee_id',
    type: 'select',
    attrs: {
      placeholder: '请选择员工',
      get options() {
        return emplyeeOptions.value;
      }
    },
  },
  { label: '采购编号', prop: 'purchase_id', type: 'input' },
];

const addPurchases = async (data: any) => {
  await store.addPurchases(data);
  await store.fetchPurchases();
};

const purchases = computed(() => store.purchases);
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
      <el-button type="success" @click="openAddDialog">新增采购记录</el-button>

      <el-table :data="purchases" style="width: 100%; margin-top: 16px;" size="large">
        <el-table-column prop="supplier_id" label="供应商编号" />
        <el-table-column prop="product_id" label="商品编号" />
        <el-table-column prop="purchase_date" label="采购日期" />
        <el-table-column prop="quantity" label="数量" />
        <el-table-column prop="unit_price" label="单价" />
        <el-table-column prop="total_price" label="总价" />
        <el-table-column prop="employee_id" label="经办员工编号" />
        <el-table-column prop="purchase_id" label="采购编号" />

        <el-table-column label="操作" width="100">
          <template #default="{ row }">
            <el-button type="danger" size="small" @click="store.deletePurchases(row.purchase_id)">删除</el-button>
          </template>
        </el-table-column>

      </el-table>
    </el-main>
  </el-container>

  <add-dialog
    ref="dialogRef"
    title="新增采购记录"
    :formSchema="purchasesSchema"
    :submitHandler="addPurchases"
  />
</template>