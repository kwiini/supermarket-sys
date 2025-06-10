<template>
  <el-aside class="w-[13%] mx-2 shadow-none bg-transparent p-4">
    <el-menu class="space-y-5" router background-color="transparent">
      <el-menu-item index="/" class="custom-item">首页</el-menu-item>
      <el-menu-item index="/members" class="custom-item">会员管理</el-menu-item>
      <el-menu-item index="/products" class="custom-item">产品管理</el-menu-item>
      <el-menu-item index="/sales" class="custom-item">销售管理</el-menu-item>
      <el-menu-item index="/purchases" class="custom-item">采购管理</el-menu-item>
      <el-menu-item index="/suppliers" class="custom-item">供应商管理</el-menu-item>
      <el-menu-item index="/inventory" class="custom-item">库存管理</el-menu-item>
    </el-menu>
  </el-aside>
</template>

<style scoped>
:deep(.el-menu) {
  border-right: none !important;
  background-color: transparent; 
  box-shadow: none;             
}

:deep(.custom-item) {
  font-size: 16px;
  height: 48px;
  background-color: #fff;  
  border-radius: 8px;     
  padding: 10px 15px;       
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05); 
  transition: all 0.3s ease;
}

:deep(.custom-item:hover) {
  background-color: #fefefe;  
  color: #23c62b;      
  transform: translateY(-3px) scale(1.08); 
}

:deep(.el-menu-item.is-active) {
  background-color: #fefefe !important;
  color: #23c62b !important;   
  font-weight: 600;
  border: none !important; 
}
</style>
