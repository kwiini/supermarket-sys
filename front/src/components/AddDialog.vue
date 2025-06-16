<script setup lang="ts">
import { ref, reactive } from 'vue';
import { ElMessage } from 'element-plus';
import dayjs from 'dayjs';

export interface FieldSchema {
  label: string;
  prop: string;
  type?: 'input' | 'select' | 'date' | 'number';
  attrs?: Record<string, any>;
}

const props = defineProps<{
  title: string;
  formSchema: FieldSchema[];
  rules?: Record<string, any>;
  submitHandler: (data: Record<string, any>) => Promise<void>;
}>();

const visible = ref(false);
const loading = ref(false);
const formData = reactive<Record<string, any>>({});
const formRef = ref();

function open(initialData: Record<string, any> = {}) {
  visible.value = true;
  props.formSchema.forEach(item => {
    formData[item.prop] = initialData[item.prop] ?? '';
  });
}

function getComponent(type?: string) {
  switch (type) {
    case 'select':
      return 'el-select';
    case 'date':
      return 'el-date-picker';
    default:
      return 'el-input';
  }
}

async function handleSubmit() {
  loading.value = true;
  try {
    await formRef.value?.validate();
    const submitData = { ...formData };

    props.formSchema.forEach(field => {
      if (field.type === 'date' && submitData[field.prop] instanceof Date) {
        submitData[field.prop] = dayjs(submitData[field.prop]).format('YYYY-MM-DD');
      }
    });

    // console.log(submitData);

    await props.submitHandler(submitData);
    ElMessage.success('提交成功');
    visible.value = false;
  } catch (err) {
    if (err !== 'cancel') {
      ElMessage.error('提交失败');
    }
  } finally {
    loading.value = false;
  }
}

defineExpose({ open });
</script>

<template>
  <el-dialog
    v-model="visible"
    :title="title"
    width="600px"
    class="rounded-xl"
    style="background: linear-gradient(to bottom left, #a7f3d0 , #d1fae5, #f0fdf4);"
    :close-on-click-modal="false"
  >
    <el-form
      ref="formRef"
      :model="formData"
      :rules="props.rules"
      label-width="100px"
      class="px-2 pt-2 pb-1"
    >
      <el-form-item
        v-for="item in formSchema"
        :key="item.prop"
        :label="item.label"
        :prop="item.prop"
        class="mb-4"
      >
        <component
          :is="getComponent(item.type)"
          v-model="formData[item.prop]"
          v-bind="item.attrs || {}"
          class="w-full"
          :placeholder="item.attrs?.placeholder || `请输入${item.label}`"
          :clearable="true"
        >
          <el-option
            v-if="item.type === 'select' && item.attrs?.options"
            v-for="option in item.attrs.options"
            :key="option.value"
            :label="option.label"
            :value="option.value"
          />
        </component>
      </el-form-item>
    </el-form>

    <template #footer>
      <div class="flex justify-end gap-2 px-2 pb-2">
        <el-button @click="visible = false">取消</el-button>
        <el-button type="success" :loading="loading" @click="handleSubmit">提交</el-button>
      </div>
    </template>
  </el-dialog>
</template>
