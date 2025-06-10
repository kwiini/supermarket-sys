<template>
  <el-header class="shadow-lg h-18">
    <div class="flex justify-between items-center h-full px-1">
      <h1 class="text-3xl font-semibold text-green-600">超超批发系统</h1>
      <ElButton class="bg-white text-green-600 hover:bg-green-600 hover:text-white border-none rounded-lg transition-colors duration-300">
        登出
      </ElButton>
    </div>
  </el-header>
</template>

<style scoped>
.el-header {
  background: linear-gradient(90deg, #f0fdf4 0%, #a7f3d0 50%, #34d399 100%);
}

.el-header .el-button {
  transition: all 0.3s ease;
}

.el-header .el-button:hover {
  background-color: #34d399;
  color: white;
}

/* 响应式 */
@media (max-width: 768px) {
  .el-header {
    padding: 10px;
  }
}
</style>
