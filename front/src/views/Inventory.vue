<script setup lang="ts">
import { onMounted, computed, ref } from 'vue';
import { useInventoryStore, useProductStore } from '../stores/index';
import AddDialog from '../components/AddDialog.vue';
import type { FieldSchema } from '../components/AddDialog.vue';

const store = useInventoryStore();
const productStore = useProductStore();
const dialogRef = ref();

onMounted(() => {
  store.fetchInventory();
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

const inventorySchema: FieldSchema[] = [
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
  { label: '批次号', prop: 'batch_number', type: 'input' },
  { label: '生产日期', prop: 'production_date', type: 'date', attrs: { placeholder: '请选择生产日期'} },
  { label: '过期日期', prop: 'expiry_date', type: 'date', attrs: { placeholder: '请选择过期日期' } },
  { label: '数量', prop: 'quantity', type: 'input', attrs: { type: 'number', min: 0 } },
  { label: '存放位置', prop: 'location', type: 'input' },
  { label: '库存编号', prop: 'inventory_id', type: 'input' },
];

const addInventory = async (data: any) => {
  await store.addInventory(data);
  await store.fetchInventory();
};

const inventory = computed(() => store.inventory);
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
      <h2 class="m-0 font-bold tracking-wide">库存管理</h2>
    </el-header>

    <el-main class="mt-5 p-4 bg-gray-50 rounded-lg shadow-inner">
      <el-button type="success" @click="openAddDialog">新增库存</el-button>

      <el-table :data="inventory" style="width: 100%; margin-top: 16px;" class="bg-white rounded-md shadow" size="large">
        <el-table-column prop="product_id" label="商品编号" />
        <el-table-column prop="batch_number" label="批次号" />
        <el-table-column prop="production_date" label="生产日期" />
        <el-table-column prop="expiry_date" label="过期日期" />
        <el-table-column prop="quantity" label="数量" />
        <el-table-column prop="location" label="存放位置" />
        <el-table-column prop="inventory_id" label="库存编号" />

        <el-table-column label="操作" width="100">
          <template #default="{ row }">
            <el-button type="danger" size="small" @click="store.deleteInventory(row.inventory_id)">删除</el-button>
          </template>
        </el-table-column>
        
      </el-table>
    </el-main>
  </el-container>

  <add-dialog
    ref="dialogRef"
    title="新增库存记录"
    :formSchema="inventorySchema"
    :submitHandler="addInventory"
  />
</template>