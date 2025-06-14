<script setup lang="ts">
import { onMounted, computed, ref } from 'vue';
import { useSaleDetailStore, useProductStore } from '../stores/index';
import AddDialog from '../components/AddDialog.vue';
import type { FieldSchema } from '../components/AddDialog.vue';

const store = useSaleDetailStore();
const productStore = useProductStore();
const dialogRef = ref();

onMounted(() => {
  store.fetchSalesDetail();
  productStore.fetchProducts();
});

const openAddDialog = () => {
  dialogRef.value.open();
};

const productOptions = computed(() =>
  productStore.products.map(p => ({
    label: `${p.product_id} - ${p.name}`,
    value: p.product_id,
  }))
);

const salesDetailSchema: FieldSchema[] = [
  { label: '销售编号', prop: 'sale_id', type: 'input' },
  {
    label: '商品编号',
    prop: 'product_id',
    type: 'select',
    attrs: {
      placeholder: '请选择商品',
      get options() {
        return productOptions.value;
      }
    },
  },
  { label: '数量', prop: 'quantity', type: 'number', attrs: { min: 1 } },
  { label: '单价', prop: 'unit_price', type: 'number', attrs: { min: 0 } },
  { label: '小计金额', prop: 'subtotal', type: 'number', attrs: { min: 0} },
  { label: '明细编号', prop: 'detail_id', type: 'input' }
];

const addSalesDetail = async (data: any) => {
  await store.addSalesDetail(data);
  await store.fetchSalesDetail();
};

const salesDetail = computed(() => store.salesDetail);
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
      <h2 class="m-0 font-bold tracking-wide">销售明细管理</h2>
    </el-header>
    
    <el-main class="mt-5 p-4 bg-gray-50 rounded-lg shadow-inner">
      <el-button type="success" @click="openAddDialog">新增销售明细</el-button>

      <el-table :data="salesDetail" style="width: 100%; margin-top: 16px;" size="large">
        <el-table-column prop="sale_id" label="销售编号" />
        <el-table-column prop="product_id" label="商品编号" />
        <el-table-column prop="quantity" label="数量" />
        <el-table-column prop="unit_price" label="单价" />
        <el-table-column prop="subtotal" label="小计金额" />
        <el-table-column prop="detail_id" label="明细编号" />

        <el-table-column label="操作" width="100">
          <template #default="{ row }">
            <el-button type="danger" size="small" @click="store.deleteSalesDetail(row.detail_id)">删除</el-button>
          </template>
        </el-table-column>

      </el-table>
    </el-main>
  </el-container>

  <add-dialog
    ref="dialogRef"
    title="新增销售明细"
    :formSchema="salesDetailSchema"
    :submitHandler="addSalesDetail"
  />
</template>