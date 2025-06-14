<script setup lang="ts">
import { onMounted, computed, ref } from 'vue';
import { useProductStore } from '../stores/index';
import AddDialog from '../components/AddDialog.vue';
import type { FieldSchema } from '../components/AddDialog.vue';

const store = useProductStore();
const dialogRef = ref();

onMounted(() => {
  store.fetchProducts();
});

const openAddDialog = () => {
  dialogRef.value.open();
};

const productsSchema: FieldSchema[] = [
  { label: '商品名称', prop: 'name', type: 'input' },
  { label: '类别', prop: 'category', type: 'input' },
  { label: '进货价', prop: 'purchase_price', type: 'input', attrs: { min: 0 } },
  { label: '售价', prop: 'selling_price', type: 'input', attrs: { min: 0 } },
  { label: '描述', prop: 'description', type: 'input' },
  { label: '商品编号', prop: 'product_id', type: 'input' },
];

const addProducts = async (data: any) => {
  await store.addProducts(data);
  await store.fetchProducts();
};

const products = computed(() => store.products);
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
      <h2 class="m-0 font-bold tracking-wide">商品管理</h2>
    </el-header>

    <el-main class="mt-5 p-4 bg-gray-50 rounded-lg shadow-inner">
      <el-button type="success" @click="openAddDialog">新增商品</el-button>

      <el-table :data="products" style="width: 100%; margin-top: 16px;" size="large">
        <el-table-column prop="name" label="商品名称" />
        <el-table-column prop="category" label="类别" />
        <el-table-column prop="purchase_price" label="进货价" />
        <el-table-column prop="selling_price" label="售价" />
        <el-table-column prop="description" label="描述" />
        <el-table-column prop="product_id" label="商品编号" />

        <el-table-column label="操作" width="100">
          <template #default="{ row }">
            <el-button type="danger" size="small" @click="store.deleteProducts(row.product_id)">删除</el-button>
          </template>
        </el-table-column>

      </el-table>
    </el-main>
  </el-container>

  <add-dialog
    ref="dialogRef"
    title="新增商品"
    :formSchema="productsSchema"
    :submitHandler="addProducts"
  />
</template>

<style scoped>
.el-header {
  background-color: #409EFF;
  color: #fff;
  padding: 20px;
  text-align: center;
}
</style>