// ATILOK Product Taxonomy
// All parts use prefix "ATL-" followed by category code and sequence

export interface Product {
  id: string;
  sku: string;
  name: string;
  category: string;
  description: string;
  price: number;
  minOrder: number;
  inStock: boolean;
  specifications?: string[];
  image?: string;
}

export const productCategories = [
  { id: 'ENG', name: 'Engine Systems', icon: '⚙️' },
  { id: 'DRV', name: 'Drivetrain', icon: '🔧' },
  { id: 'SUS', name: 'Suspension & Steering', icon: '🛞' },
  { id: 'ELC', name: 'Electrical', icon: '⚡' },
  { id: 'CAB', name: 'Cab & Body', icon: '🚛' },
  { id: 'MNT', name: 'Maintenance', icon: '🔩' },
];

export const products: Product[] = [
  // Engine Systems
  {
    id: '1',
    sku: 'ATL-ENG-001',
    name: 'ATILOK Precision Brake Disc',
    category: 'ENG',
    description: 'Engineered to OEM standards for consistent performance. High-grade cast iron construction with precision machining for optimal heat dissipation and extended service life.',
    price: 125.00,
    minOrder: 2,
    inStock: true,
    specifications: [
      'Diameter: 420mm',
      'Thickness: 45mm',
      'Material: High-grade cast iron',
      'OEM Compatible: Yes',
      'Warranty: 12 months'
    ]
  },
  {
    id: '2',
    sku: 'ATL-ENG-002',
    name: 'ATILOK Heavy-Duty Brake Pad Set',
    category: 'ENG',
    description: 'Premium friction material formulation for superior stopping power. Designed for heavy commercial vehicles operating in demanding conditions.',
    price: 85.00,
    minOrder: 4,
    inStock: true,
    specifications: [
      'Friction Rating: ECE R90',
      'Temperature Range: -40°C to 600°C',
      'Low Noise Design',
      'OEM Compatible: Yes'
    ]
  },
  {
    id: '3',
    sku: 'ATL-ENG-003',
    name: 'ATILOK Air Filter Assembly',
    category: 'ENG',
    description: 'High-efficiency filtration system protecting engine components. Multi-layer design ensures optimal airflow while maintaining superior particle capture.',
    price: 45.00,
    minOrder: 6,
    inStock: true,
    specifications: [
      'Filtration Efficiency: 99.9%',
      'Service Interval: 50,000 miles',
      'OEM Compatible: Yes'
    ]
  },

  // Drivetrain
  {
    id: '4',
    sku: 'ATL-DRV-001',
    name: 'ATILOK Kingpin Assembly',
    category: 'DRV',
    description: 'Precision-engineered kingpin assembly for heavy-duty applications. Hardened steel construction with precision tolerances for smooth operation and extended durability.',
    price: 350.00,
    minOrder: 1,
    inStock: true,
    specifications: [
      'Material: Hardened steel',
      'Load Rating: 25,000kg',
      'OEM Compatible: Yes',
      'Warranty: 24 months'
    ]
  },
  {
    id: '5',
    sku: 'ATL-DRV-002',
    name: 'ATILOK Drive Shaft Universal Joint',
    category: 'DRV',
    description: 'Heavy-duty universal joint designed for maximum torque transmission. Sealed design protects internal components from contamination.',
    price: 180.00,
    minOrder: 2,
    inStock: true,
    specifications: [
      'Torque Rating: 3,500 Nm',
      'Sealed Design',
      'OEM Compatible: Yes'
    ]
  },
  {
    id: '6',
    sku: 'ATL-DRV-003',
    name: 'ATILOK Differential Gear Set',
    category: 'DRV',
    description: 'Precision-cut differential gears for smooth power distribution. Manufactured to exacting tolerances for quiet operation and long service life.',
    price: 650.00,
    minOrder: 1,
    inStock: true,
    specifications: [
      'Gear Ratio: Various available',
      'Material: Case-hardened steel',
      'OEM Compatible: Yes'
    ]
  },

  // Suspension & Steering
  {
    id: '7',
    sku: 'ATL-SUS-001',
    name: 'ATILOK Heavy-Duty Shock Absorber',
    category: 'SUS',
    description: 'Performance shock absorber engineered for commercial vehicle applications. Advanced valving technology provides optimal ride comfort and stability.',
    price: 95.00,
    minOrder: 2,
    inStock: true,
    specifications: [
      'Load Rating: 7,500kg per unit',
      'Gas Pressurised',
      'OEM Compatible: Yes'
    ]
  },
  {
    id: '8',
    sku: 'ATL-SUS-002',
    name: 'ATILOK Steering Tie Rod End',
    category: 'SUS',
    description: 'Precision steering component ensuring accurate vehicle control. Greaseable design for extended service intervals.',
    price: 55.00,
    minOrder: 4,
    inStock: true,
    specifications: [
      'Material: Forged steel',
      'Greaseable Design',
      'OEM Compatible: Yes'
    ]
  },
  {
    id: '9',
    sku: 'ATL-SUS-003',
    name: 'ATILOK Leaf Spring Set',
    category: 'SUS',
    description: 'Heavy-duty leaf spring assembly for maximum load capacity. Multi-leaf design provides progressive spring rate for optimal ride characteristics.',
    price: 420.00,
    minOrder: 1,
    inStock: true,
    specifications: [
      'Load Capacity: 12,000kg',
      'Multi-Leaf Design',
      'OEM Compatible: Yes'
    ]
  },

  // Electrical
  {
    id: '10',
    sku: 'ATL-ELC-001',
    name: 'ATILOK Heavy-Duty Alternator',
    category: 'ELC',
    description: 'High-output alternator for commercial vehicle electrical systems. Designed to handle demanding accessory loads while maintaining battery charge.',
    price: 380.00,
    minOrder: 1,
    inStock: true,
    specifications: [
      'Output: 24V, 150A',
      'Brushless Design',
      'OEM Compatible: Yes'
    ]
  },
  {
    id: '11',
    sku: 'ATL-ELC-002',
    name: 'ATILOK Starter Motor',
    category: 'ELC',
    description: 'Heavy-duty starter motor with high torque output for reliable engine starting in all conditions. Sealed design protects against environmental contamination.',
    price: 320.00,
    minOrder: 1,
    inStock: true,
    specifications: [
      'Voltage: 24V',
      'Power: 4.5kW',
      'OEM Compatible: Yes'
    ]
  },

  // Cab & Body
  {
    id: '12',
    sku: 'ATL-CAB-001',
    name: 'ATILOK Heavy-Duty Door Hinge Set',
    category: 'CAB',
    description: 'Reinforced door hinge assembly for commercial vehicle applications. Designed to withstand repeated opening cycles and heavy door weights.',
    price: 75.00,
    minOrder: 2,
    inStock: true,
    specifications: [
      'Material: Steel with bronze bushings',
      'Load Rating: 150kg per door',
      'OEM Compatible: Yes'
    ]
  },
  {
    id: '13',
    sku: 'ATL-CAB-002',
    name: 'ATILOK Windscreen Wiper Motor',
    category: 'CAB',
    description: 'Heavy-duty wiper motor for reliable operation in all weather conditions. High-torque design ensures effective clearing even under heavy load.',
    price: 125.00,
    minOrder: 1,
    inStock: true,
    specifications: [
      'Voltage: 24V',
      'Torque: 25 Nm',
      'OEM Compatible: Yes'
    ]
  },

  // Maintenance
  {
    id: '14',
    sku: 'ATL-MNT-001',
    name: 'ATILOK Engine Oil Filter',
    category: 'MNT',
    description: 'High-efficiency oil filtration system protecting engine internals. Synthetic media provides superior contaminant capture and extended service intervals.',
    price: 18.00,
    minOrder: 12,
    inStock: true,
    specifications: [
      'Filtration: 10 microns',
      'Service Interval: 25,000 miles',
      'OEM Compatible: Yes'
    ]
  },
  {
    id: '15',
    sku: 'ATL-MNT-002',
    name: 'ATILOK Fuel Filter Assembly',
    category: 'MNT',
    description: 'Heavy-duty fuel filtration system protecting injection components. Water separator design removes contaminants and moisture from fuel supply.',
    price: 35.00,
    minOrder: 6,
    inStock: true,
    specifications: [
      'Filtration: 2 microns',
      'Water Separator Included',
      'OEM Compatible: Yes'
    ]
  },
];

export function getProductsByCategory(categoryId: string): Product[] {
  return products.filter(p => p.category === categoryId);
}

export function getProductBySku(sku: string): Product | undefined {
  return products.find(p => p.sku === sku);
}
