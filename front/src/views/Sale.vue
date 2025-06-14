<script setup lang="ts">
import { onMounted, computed, ref } from 'vue';
import { useSaleStore, useMemberStore } from '../stores/index';
import AddDialog from '../components/AddDialog.vue';
import type { FieldSchema } from '../components/AddDialog.vue';

const store = useSaleStore();
const memberStore = useMemberStore();
const dialogRef = ref();

onMounted(() => {
  store.fetchSales();
  memberStore.fetchMembers();
});

const openAddDialog = () => {
  dialogRef.value.open();
};

const memberOptions = computed(() =>
  memberStore.members.map(m => ({
    label: `${m.member_id} - ${m.name}`,
    value: m.member_id,
  }))
);

const salesSchema: FieldSchema[] = [
  {
    label: '会员编号',
    prop: 'member_id',
    type: 'select',
    attrs: {
      placeholder: '请选择商品',
      get options() {
        return memberOptions.value;
      }
    },
  },
  { label: '销售日期', prop: 'sale_date', type: 'date', attrs: { placeholder: '选择销售日期' } },
  { label: '总金额', prop: 'total_amount', type: 'number', attrs: { min: 0 } },
  { label: '折扣金额', prop: 'discount_amount', type: 'number', attrs: { min: 0 } },
  {
    label: '支付方式',
    prop: 'payment_method',
    type: 'select',
    attrs: {  options: [
      { label: '现金', value: '现金' },
      { label: '移动支付', value: '移动支付' },
      { label: '信用卡', value: '信用卡' },
    ] }
  },
  { label: '收银员编号', prop: 'employee_id', type: 'input' },
  { label: '销售编号', prop: 'sale_id', type: 'input' },
];



const addSales = async (data: any) => {
  await store.addSales(data);
  await store.fetchSales();
};

const sales = computed(() => store.sales);
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
      <h2 class="m-0 font-bold tracking-wide">销售管理</h2>
    </el-header>
    
    <el-main class="mt-5 p-4 bg-gray-50 rounded-lg shadow-inner">
      <el-button type="success" @click="openAddDialog">新增销售记录</el-button>

      <el-table :data="sales" style="width: 100%; margin-top: 16px;" size="large">
        <el-table-column prop="member_id" label="会员编号" />
        <el-table-column prop="sale_date" label="销售日期" />
        <el-table-column prop="total_amount" label="总金额" />
        <el-table-column prop="discount_amount" label="折扣金额" />
        <el-table-column prop="payment_method" label="支付方式" />
        <el-table-column prop="employee_id" label="收银员编号" />
        <el-table-column prop="sale_id" label="销售编号" />

        <el-table-column label="操作" width="100">
          <template #default="{ row }">
            <el-button type="danger" size="small" @click="store.deleteSales(row.sale_id)">删除</el-button>
          </template>
        </el-table-column>
        
      </el-table>
    </el-main>
  </el-container>

  <add-dialog
    ref="dialogRef"
    title="新增销售记录"
    :formSchema="salesSchema"
    :submitHandler="addSales"
  />
</template>